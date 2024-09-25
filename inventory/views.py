from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.contrib.auth import authenticate
import logging

# Set up logging
logger = logging.getLogger('inventory')

# cache timeout
CACHE_TTL = 60 * 5 #seconds

@api_view(['POST'])
def register(request):
    """
    User registration endpoint.
    """
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        logger.info(f"User {serializer.data['username']} registered successfully.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.error(f"User registration failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """
    User login endpoint to obtain JWT tokens.
    """
    from django.contrib.auth import authenticate

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    
    if user is not None:
        refresh = RefreshToken.for_user(user)
        logger.info(f"User {username} logged in successfully.")
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
    logger.warning(f"Authentication failed for user {username}.")
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    """
    Create a new inventory item.
    """
    serializer = ItemSerializer(data=request.data)
    if Item.objects.filter(name=request.data.get('name')).exists():
        logger.error(f"Item creation failed: Item '{request.data.get('name')}' already exists.")
        return Response({'error': 'Item already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Item '{serializer.data['name']}' created successfully.")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    logger.error(f"Item creation failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_item(request, item_id):
    """
    Retrieve an inventory item. Utilizes Redis caching.
    """
    cache_key = f'item_{item_id}'
    item_data = cache.get(cache_key)

    if item_data:
        logger.info(f"Cache hit for item ID {item_id}.")
        return Response(item_data, status=status.HTTP_200_OK)
    else:
        logger.info(f"Cache miss for item ID {item_id}. Fetching from DB.")
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(item)
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)  # Cache for 5 minutes
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, item_id):
    """
    Update an existing inventory item.
    """
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        # Update cache
        cache_key = f'item_{item_id}'
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
        logger.info(f"Item ID {item_id} updated successfully.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    logger.error(f"Item update failed for ID {item_id}: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, item_id):
    """
    Delete an inventory item.
    """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    
    # Remove from cache
    cache_key = f'item_{item_id}'
    cache.delete(cache_key)
    logger.info(f"Item ID {item_id} deleted successfully.")
    return Response({'message': 'Item deleted successfully.'}, status=status.HTTP_200_OK)