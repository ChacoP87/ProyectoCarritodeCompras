# Generated by Django 4.2.11 on 2024-03-21 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_tienda_alter_producto_options_producto_perecedero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('fecha', models.DateField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.producto')),
                ('tienda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.tienda')),
            ],
        ),
    ]