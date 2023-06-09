# Generated by Django 4.1 on 2023-04-22 10:01

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_productrate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='provider',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping_from',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping_to',
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_destinations',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_origin',
            field=django_countries.fields.CountryField(default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
