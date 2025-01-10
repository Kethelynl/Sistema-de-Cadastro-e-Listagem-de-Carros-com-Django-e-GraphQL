from django.db import models

class Car(models.Model):
    SERVICE_CHOICES = [
        ('wash', 'lavagem simples'),
        ('polish', 'polimento'),
        ('wax', "encerramento"),
    ]

    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.license_plate}"
