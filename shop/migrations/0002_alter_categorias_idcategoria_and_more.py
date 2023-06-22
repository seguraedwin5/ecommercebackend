# Generated by Django 4.2.2 on 2023-06-21 02:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='IdCategoria',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productos',
            name='IdProducto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='IdProveedor',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('IdMovimiento', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField(default=datetime.date(2023, 6, 20))),
                ('Tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Salida')], max_length=20)),
                ('Descripcion', models.TextField()),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='UsuarioMovimiento')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesMovimientoProducto',
            fields=[
                ('IdDetalle', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.BigIntegerField()),
                ('PrecioTotal', models.DecimalField(decimal_places=2, max_digits=20)),
                ('IdMovimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.movimientos')),
                ('IdProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productos')),
            ],
        ),
    ]