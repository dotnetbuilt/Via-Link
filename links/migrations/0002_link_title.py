# Generated by Django 5.0.4 on 2024-04-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]