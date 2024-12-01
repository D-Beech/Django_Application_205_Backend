# Generated by Django 4.2 on 2024-11-07 09:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_superchecker_project', '0003_countdown_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('contents', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
            ],
        ),
    ]