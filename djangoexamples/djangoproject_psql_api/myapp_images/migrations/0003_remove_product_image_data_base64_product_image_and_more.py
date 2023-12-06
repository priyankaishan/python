# Generated by Django 4.2.7 on 2023-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_images', '0002_remove_product_image_product_image_data_base64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_data_base64',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_data_bytea',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
