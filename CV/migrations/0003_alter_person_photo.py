# Generated by Django 3.2.9 on 2021-11-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0002_alter_person_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to="Person's photo", verbose_name='Avatar'),
        ),
    ]