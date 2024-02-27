# Generated by Django 4.2.7 on 2024-02-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.CharField(choices=[('sala_espera', 'Sala de Espera'), ('pendiente', 'Pendiente')], default='sala_espera', max_length=20),
        ),
    ]
