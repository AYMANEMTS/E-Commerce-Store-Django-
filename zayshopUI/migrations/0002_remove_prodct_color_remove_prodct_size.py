# Generated by Django 4.1.7 on 2023-02-17 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zayshopUI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='prodct',
            name='size',
        ),
    ]