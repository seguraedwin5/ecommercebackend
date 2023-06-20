# Generated by Django 4.2.2 on 2023-06-15 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('Id', models.IntegerField(max_length=50, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Id', models.IntegerField(max_length=50, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Cantidad', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoxCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categoria')),
                ('IdProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.producto')),
            ],
        ),
    ]