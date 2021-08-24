# Generated by Django 3.2.6 on 2021-08-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_taken', models.DateTimeField(verbose_name='date taken')),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='pressure')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='temperature')),
                ('altitute', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='altitude')),
            ],
        ),
    ]
