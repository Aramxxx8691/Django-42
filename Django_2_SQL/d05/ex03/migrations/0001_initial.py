# Generated by Django 3.2.25 on 2024-10-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64, unique=True)),
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField(null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
            options={
                'db_table': 'ex03_movies',
            },
        ),
    ]
