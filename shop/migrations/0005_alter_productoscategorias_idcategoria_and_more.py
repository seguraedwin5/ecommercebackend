# Generated by Django 4.2.2 on 2023-06-21 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_productoscategorias_idcategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoscategorias',
            name='IdCategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', related_query_name='categoria_id', to='shop.categorias'),
        ),
        migrations.AlterField(
            model_name='productoscategorias',
            name='IdProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', related_query_name='producto_id', to='shop.productos'),
        ),
    ]
