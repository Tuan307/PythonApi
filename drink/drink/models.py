from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.name + ' ' + self.description
