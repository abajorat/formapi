# Generated by Django 3.1.3 on 2020-11-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True)),
                ('position', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]