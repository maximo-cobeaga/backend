# Generated by Django 4.2.3 on 2023-07-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_productos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='oferta',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productos',
            name='precioDolar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
