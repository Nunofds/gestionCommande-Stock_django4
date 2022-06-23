from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=250, null=True)
    phone = models.CharField(max_length=20, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

