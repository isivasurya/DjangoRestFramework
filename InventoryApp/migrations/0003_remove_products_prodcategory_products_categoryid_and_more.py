# Generated by Django 5.1.1 on 2024-09-09 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryApp', '0002_category_products_prodcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Prodcategory',
        ),
        migrations.AddField(
            model_name='products',
            name='categoryid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InventoryApp.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
