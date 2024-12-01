# Generated by Django 4.2 on 2024-11-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_superchecker_project', '0002_product_img_product_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countdown_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dollars', models.SmallIntegerField()),
                ('cents', models.SmallIntegerField()),
                ('img', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]