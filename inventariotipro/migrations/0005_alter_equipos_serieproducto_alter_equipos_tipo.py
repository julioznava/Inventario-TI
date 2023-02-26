# Generated by Django 4.1.7 on 2023-02-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariotipro', '0004_alter_monitores_serieproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='serieproducto',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='tipo',
            field=models.CharField(blank=True, choices=[['DESKTOP', 'DESKTOP'], ['LAPTOP', 'LAPTOP']], max_length=50, null=True),
        ),
    ]
