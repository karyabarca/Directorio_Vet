from django.db import models

class Veterinaria(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    horario = models.CharField(max_length=255)
    admite_emergencias = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

