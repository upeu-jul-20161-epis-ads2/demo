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

# angel

# angel
# edwin alvarado

# angel

# otra

# Shiane


class Persona(models.models):
    usuario = models.foreignKey(User)
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return nombre
# Vladimir (NotThisTime...)

# ################ subiendo tareas #############
