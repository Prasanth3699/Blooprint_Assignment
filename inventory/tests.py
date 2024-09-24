from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item
from rest_framework_simplejwt.tokens import RefreshToken

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        # Obtain JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.auth_header = f'Bearer {self.access_token}'
        # Create an item
        self.item = Item.objects.create(
            name='Test Item',
            description='A test item.',
            quantity=10,
            price=99.99,
            category='electronics'
        )

    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(username='newuser').exists(), True)

    def test_login_user(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'pass1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_create_item(self):
        url = reverse('create_item')
        data = {
            'name': 'New Item',
            'description': 'New item description.',
            'quantity': 5,
            'price': 49.99,
            'category': 'clothing'
        }
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.filter(name='New Item').exists(), True)
        self.assertEqual(Item.objects.get(name='New Item').quantity, 5)
        self.assertEqual(float(Item.objects.get(name='New Item').price), 49.99)
        self.assertEqual(Item.objects.get(name='New Item').category, 'clothing')

    def test_create_existing_item(self):
        url = reverse('create_item')
        data = {
            'name': 'Test Item',
            'description': 'Duplicate item.',
            'quantity': 5,
            'price': 49.99,
            'category': 'clothing'
        }
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Item already exists.')

    def test_read_item(self):
        url = reverse('read_item', kwargs={'item_id': self.item.id})
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item')
        self.assertEqual(response.data['quantity'], 10)
        self.assertEqual(float(response.data['price']), 99.99)
        self.assertEqual(response.data['category'], 'electronics')

    def test_update_item(self):
        url = reverse('update_item', kwargs={'item_id': self.item.id})
        data = {
            'name': 'Updated Item',
            'description': 'Updated description.',
            'quantity': 15,
            'price': 149.99,
            'category': 'furniture'
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.quantity, 15)
        self.assertEqual(float(self.item.price), 149.99)
        self.assertEqual(self.item.category, 'furniture')

    def test_delete_item(self):
        url = reverse('delete_item', kwargs={'item_id': self.item.id})
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())
