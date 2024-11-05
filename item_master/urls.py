from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Set up the API router
router = DefaultRouter()
router.register(r'items', views.ItemMasterViewSet, basename='itemmaster')

# Define URL patterns
urlpatterns = [
    path('create/', views.item_create_view, name='item_create'),       # Form to create an item
    path('success/', views.item_success_view, name='item_success'),     # Success page after item creation
    path('upload_excel/', views.excel_upload_view, name='upload_excel'),  # Excel upload view
    path('api/', include(router.urls)),                                # API URL path with router
    path('list/', views.item_list_view, name='item_list'),
]
