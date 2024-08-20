# Generated by Django 5.0.6 on 2024-08-20 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0002_pregunta_es_predefinida'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='notificado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='respondida',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respondida_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
