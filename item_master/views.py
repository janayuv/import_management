from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
from .models import ItemMaster, Supplier
from .forms import ItemMasterForm, ExcelUploadForm
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ItemMasterSerializer

# View to create a single item
def item_create_view(request):
    if request.method == 'POST':
        form = ItemMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_success')
    else:
        form = ItemMasterForm()
    
    return render(request, 'item_master/item_form.html', {'form': form})

# Success view
def item_success_view(request):
    return HttpResponse("<h1>Item created successfully!</h1>")

# Excel upload view

def excel_upload_view(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            try:
                df = pd.read_excel(file)  # Read the Excel file into a DataFrame
                for _, row in df.iterrows():
                    # Check if the supplier exists in the Supplier model
                    try:
                        supplier_instance = Supplier.objects.get(name=row['supplier'])  # Adjust based on actual field in Supplier
                    except Supplier.DoesNotExist:
                        messages.error(request, f"Supplier '{row['supplier']}' does not exist. Skipping this row.")
                        continue  # Skip this row if the supplier does not exist

                    # Validate unit
                    if row['unit'] not in [choice[0] for choice in ItemMaster._meta.get_field('unit').choices]:
                        messages.error(request, f"Invalid unit value '{row['unit']}' for part number '{row['part_number']}'. Skipping this row.")
                        continue  # Skip this row if the unit is invalid

                    # Create ItemMaster instance
                    ItemMaster.objects.create(
                        supplier=supplier_instance,
                        part_number=row['part_number'],
                        part_description=row['part_description'],
                        unit=row['unit'],
                        price=row['price'],
                        bcd=row['bcd'],
                        sws=row['sws'],
                        igst=row['igst'],
                        cth=row['cth'],
                    )
                messages.success(request, "Items uploaded successfully!")
                return redirect('item_list')  # Redirect to your item list view
            except Exception as e:
                messages.error(request, f"Error processing file: {e}")
    else:
        form = ExcelUploadForm()

    return render(request, 'item_master/excel_upload.html', {'form': form})

def item_list_view(request):
    items = ItemMaster.objects.all()
    return render(request, 'item_master/item_list.html', {'items': items})

# API Viewset
class ItemMasterViewSet(viewsets.ModelViewSet):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer
