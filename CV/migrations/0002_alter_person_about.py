# Generated by Django 3.2.9 on 2021-11-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='about',
            field=models.TextField(max_length=500, verbose_name='Professional summary'),
        ),
    ]