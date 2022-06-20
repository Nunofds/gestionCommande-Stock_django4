from django.db import models
from client.models import Client
from product.models import Product


class Command(models.Model):
    STATUTS = (
        ('en instance', 'en instance'),
        ('Non livré', 'Non livré'),
        ('Livré', 'Livré')
    )
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    statut = models.CharField(max_length=200, null=True, choices=STATUTS)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

