# pre_alert/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PreAlertListView.as_view(), name='pre_alert_list'),
    path('new/', views.PreAlertCreateView.as_view(), name='pre_alert_form'),
    path('<int:pk>/', views.PreAlertDetailView.as_view(), name='pre_alert_detail'),  # Correct pattern for detail view
]
