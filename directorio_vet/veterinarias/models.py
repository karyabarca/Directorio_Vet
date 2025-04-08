from django.db import models
from multiselectfield import MultiSelectField


class Veterinaria(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    horario = models.CharField(max_length=255)
    admite_emergencias = models.BooleanField(default=False)
    SERVICIOS_OPCIONES = (
        ('spa', 'Spa'),
        ('consulta', 'Consulta veterinaria'),
        ('cirugia', 'Cirugía'),
        ('farmacia', 'Farmacia'),
        ('accesorios', 'Venta de accesorios'),
        ('comida', 'Venta de comida'),
        ('domicilio', 'Servicio a domicilio'),
        ('pension', 'Pensión'),
        ('esterilizacion', 'Esterilización'),
    )

    servicios = MultiSelectField(choices=SERVICIOS_OPCIONES, blank=True)

    def __str__(self):
        return self.nombre

