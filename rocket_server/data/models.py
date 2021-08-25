from django.db import models

# Create your models here.

class Point(models.Model):
    time_taken = models.DateTimeField('date taken')
    pressure = models.DecimalField('pressure', max_digits=10, decimal_places=2)
    temperature = models.DecimalField('temperature', max_digits=10, decimal_places=2)
    altitude = models.DecimalField('altitude', max_digits=10, decimal_places=2)
