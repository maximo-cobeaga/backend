# Generated by Django 4.2.3 on 2023-07-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_remove_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='productos.productos'),
        ),
    ]