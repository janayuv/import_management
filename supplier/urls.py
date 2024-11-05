# supplier/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, supplier_create_view, supplier_success_view

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', supplier_create_view, name='supplier_create'),
    path('success/', supplier_success_view, name='supplier_success'),
]
