# Generated by Django 5.0.6 on 2024-08-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id_Pregunta'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id_Respuesta'),
        ),
    ]
