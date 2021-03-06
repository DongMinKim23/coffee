# Generated by Django 2.2.4 on 2019-11-01 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='M', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='years',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
    ]
