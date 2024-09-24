from django.urls import path
from . import views

urlpatterns = [
    # Authentication endpoints
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    # CRUD endpoints for Items
    path('items/', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.read_item, name='read_item'),
    path('items/<int:item_id>/update/', views.update_item, name='update_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
]
