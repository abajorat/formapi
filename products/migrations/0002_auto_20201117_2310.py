# Generated by Django 3.1.3 on 2020-11-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
