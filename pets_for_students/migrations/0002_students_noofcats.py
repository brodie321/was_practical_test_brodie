# Generated by Django 2.1.5 on 2024-03-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_for_students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='noOfCats',
            field=models.IntegerField(default=0),
        ),
    ]
