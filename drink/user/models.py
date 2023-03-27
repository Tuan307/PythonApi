# Create your models here.
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.name, self.email, self.mobile, self.password, self.address)
