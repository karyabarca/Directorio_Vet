from django.db import models
from multiselectfield import MultiSelectField


HORAS_OPCIONES = [
    ("06:00", "06:00 AM"),
    ("07:00", "07:00 AM"),
    ("08:00", "08:00 AM"),
    ("09:00", "09:00 AM"),
    ("10:00", "10:00 AM"),
    ("11:00", "11:00 AM"),
    ("12:00", "12:00 PM"),
    ("13:00", "01:00 PM"),
    ("14:00", "02:00 PM"),
    ("15:00", "03:00 PM"),
    ("16:00", "04:00 PM"),
    ("17:00", "05:00 PM"),
    ("18:00", "06:00 PM"),
    ("19:00", "07:00 PM"),
    ("20:00", "08:00 PM"),
    ("21:00", "09:00 PM"),
    ("22:00", "10:00 PM"),
]

apertura = models.CharField(max_length=5, choices=HORAS_OPCIONES, default="06:00")
cierre = models.CharField(max_length=5, choices=HORAS_OPCIONES, default="22:00")




class Veterinaria(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    admite_emergencias = models.BooleanField(default=False)

    apertura = models.CharField(max_length=5, choices=HORAS_OPCIONES)
    cierre = models.CharField(max_length=5, choices=HORAS_OPCIONES)

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
