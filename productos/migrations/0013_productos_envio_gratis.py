# Generated by Django 4.2.3 on 2023-07-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_productos_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='envio_gratis',
            field=models.BooleanField(default=False),
        ),
    ]
