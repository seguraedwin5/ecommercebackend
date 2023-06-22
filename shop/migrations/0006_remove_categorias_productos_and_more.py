# Generated by Django 4.2.2 on 2023-06-21 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_productoscategorias_idcategoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorias',
            name='Productos',
        ),
        migrations.AlterField(
            model_name='categorias',
            name='IdCategoria',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='idc'),
        ),
        migrations.AlterField(
            model_name='productoscategorias',
            name='IdCategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categorias'),
        ),
        migrations.AlterField(
            model_name='productoscategorias',
            name='IdProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productos'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='productos',
            field=models.ManyToManyField(related_name='miscategorias', through='shop.ProductosCategorias', to='shop.productos'),
        ),
    ]