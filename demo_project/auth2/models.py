from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    name2 = models.CharField(
        max_length=80, unique=True, null=True, blank=True
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

<<<<<<< HEAD
"""
Franklin probando .. 
"""
=======
# angel
>>>>>>> a76956ca1c8da78500ff5bc8f56dae66d652dd88
