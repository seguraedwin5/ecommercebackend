# Generated by Django 4.2.2 on 2023-06-21 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('IdCategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('IdProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Descripcion', models.TextField()),
                ('PrecioUnitario', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Stock', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('IdProveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosCategorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categorias')),
                ('IdProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productos')),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='IdProveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.proveedores'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='Productos',
            field=models.ManyToManyField(through='shop.ProductosCategorias', to='shop.productos'),
        ),
    ]
