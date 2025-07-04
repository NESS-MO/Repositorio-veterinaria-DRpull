from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from Apl.models.administrador import Administrador


class Cliente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad')
    ]

    tipo_documento = models.CharField(
        max_length=2,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='CC'
    )
    numero_documento = models.CharField(  # NUEVO CAMPO
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6)],
        null=True,
        blank=True
    )
    primer_nombre = models.CharField(max_length=250, null=True)
    primer_apellido = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=11, validators=[MinLengthValidator(7)])
    correo_electronico = models.CharField(
        max_length=250, 
        validators=[EmailValidator(message="Ingrese un correo electrónico válido")]
    )
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clientes'
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"