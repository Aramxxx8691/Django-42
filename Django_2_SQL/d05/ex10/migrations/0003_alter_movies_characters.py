# Generated by Django 3.2.25 on 2024-08-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0002_auto_20240813_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='characters',
            field=models.ManyToManyField(related_name='characters', to='ex10.People'),
        ),
    ]