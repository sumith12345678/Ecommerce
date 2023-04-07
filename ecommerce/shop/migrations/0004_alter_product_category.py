# Generated by Django 4.1.4 on 2023-01-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Sm', 'Smart'), ('Di', 'Digital'), ('An', 'Analog'), ('Sp', 'Sports'), ('Qu', 'Quartz'), ('Ch', 'Chronograph')], max_length=200, null=True),
        ),
    ]
