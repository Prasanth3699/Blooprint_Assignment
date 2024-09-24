from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','quantity','price','category')
    search_fields = ('name',)
    ordering = ('name',)