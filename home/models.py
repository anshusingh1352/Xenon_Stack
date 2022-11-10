from django.db import models

# Create your models here.
class savedata_model(models.Model):
    first_name =models.CharField(max_length =50)
    last_name =models.CharField(max_length =50)
    birthday =models.CharField(max_length =50)
    email =models.CharField(max_length =80)
    phone =models.CharField(max_length =50)
    password =models.CharField(max_length =50)
    phone =models.CharField(max_length =50)
    country =models.CharField(max_length =50)

class savedata_contact(models.Model):
    name =models.CharField(max_length =50)
    email =models.CharField(max_length =80)
    phone =models.CharField(max_length =50)
    message =models.CharField(max_length =100)
