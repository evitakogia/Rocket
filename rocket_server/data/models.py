from django.db import models

# Create your models here.

class Point(models.Model):
    time_taken = models.DateTimeField('date taken')
    pressure = models.DecimalField('pressure', max_digits=5, decimal_places=2)
    temperature = models.DecimalField('temperature', max_digits=5, decimal_places=2)
    altitute = models.DecimalField('altitude', max_digits=5, decimal_places=2)
