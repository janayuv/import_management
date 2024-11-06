from django.db import models
from supplier.models import Supplier

class PreAlert(models.Model):
    # Invoice Details
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=100)
    date = models.DateField()
    goods = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    inv_value = models.DecimalField(max_digits=15, decimal_places=3)

    # BL/AWB Information
    forwarder = models.CharField(max_length=100)
    incoterm = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)
    bl_awb_no = models.CharField(max_length=100)
    bl_awb_date = models.DateField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    etd = models.DateField()
    eta = models.DateField()
    kind_of = models.CharField(max_length=50)
    container_no = models.CharField(max_length=100)
    nop = models.CharField(max_length=100)
    vsl = models.CharField(max_length=100)

    # BOE Details
    boe_no = models.CharField(max_length=100)
    boe_date = models.DateField()
    ex_rate = models.DecimalField(max_digits=10, decimal_places=4)
    dutypaid = models.DecimalField(max_digits=10, decimal_places=2)
    boe_frt = models.DecimalField(max_digits=10, decimal_places=2)
    boe_exw = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PreAlert {self.invoice_no} - {self.supplier}"
