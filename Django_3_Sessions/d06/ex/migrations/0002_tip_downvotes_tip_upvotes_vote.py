# Generated by Django 4.2 on 2024-09-14 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tip',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(choices=[('U', 'Upvote'), ('D', 'Downvote')], max_length=1)),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ex.tip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'tip')},
            },
        ),
    ]
