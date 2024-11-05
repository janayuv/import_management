# supplier/views.py

from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import SupplierSerializer
from django.db import IntegrityError

# ViewSet for handling API requests
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# View for creating a supplier via a form
def supplier_create_view(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('supplier_success')  # Redirect to success view
            except IntegrityError:
                form.add_error(None, "This supplier already exists. Please use a different name or email.")
    else:
        form = SupplierForm()

    return render(request, 'supplier/supplier_form.html', {'form': form})

# Success view to display after supplier creation
def supplier_success_view(request):
    return HttpResponse("<h1>Supplier created successfully!</h1>")
