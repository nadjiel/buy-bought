from django.db import models

# Defines the Product model, which provides ORM features.


class Product(models.Model):

    name = models.CharField(max_length=128)

    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
