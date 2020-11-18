from django.db import models
from django.db.models import DateTimeField, FloatField, Model, TextField, IntegerField, ImageField
from django.urls import reverse


# Create your models here.
class Product(Model):
    code = TextField(blank=True)
    position = IntegerField()
    quantity = IntegerField()
    image = ImageField(upload_to='')
    price = FloatField()
    description = TextField(blank=True)

    def get_absolute_url(self):
        return reverse('product_list')