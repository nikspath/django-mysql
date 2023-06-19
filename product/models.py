from django.db import models

# Create your models here.


class Product(models.Model):
    prod_name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.prod_name