from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import PreAlert
from .forms import PreAlertForm

class PreAlertListView(ListView):
    model = PreAlert
    template_name = 'pre_alert/pre_alert_list.html'
    context_object_name = 'pre_alerts'

class PreAlertCreateView(CreateView):
    model = PreAlert
    form_class = PreAlertForm
    template_name = 'pre_alert/pre_alert_form.html'
    success_url = reverse_lazy('pre_alert_list')  # Redirect to list view after successful creation

class PreAlertDetailView(DetailView):
    model = PreAlert
    template_name = 'pre_alert/pre_alert_detail.html'  # Adjust path as needed
    context_object_name = 'prealert'  # This is the object name in the template
