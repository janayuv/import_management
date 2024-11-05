from django.db import models
from supplier.models import Supplier  # Assuming `Supplier` model is in supplier app

class ItemMaster(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="items")
    part_number = models.CharField(max_length=50)
    part_description = models.CharField(max_length=100, unique=True)  # Updated field
    unit = models.CharField(max_length=10, choices=[('EA', 'Each'), ('KGS', 'Kilograms'), ('LTRS', 'Liters')])
    price = models.DecimalField(max_digits=15, decimal_places=4)
    bcd = models.DecimalField(max_digits=10, decimal_places=4)
    sws = models.DecimalField(max_digits=10, decimal_places=4)
    igst = models.DecimalField(max_digits=10, decimal_places=4)
    cth = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.part_number} - {self.part_description}"
