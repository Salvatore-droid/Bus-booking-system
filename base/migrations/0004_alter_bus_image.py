# Generated by Django 5.1.7 on 2025-03-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_bus_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='image',
            field=models.ImageField(blank=True, default='bus.jpg', upload_to='buses/'),
        ),
    ]
