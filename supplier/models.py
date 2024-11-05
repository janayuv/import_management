from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=20, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    bank = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
