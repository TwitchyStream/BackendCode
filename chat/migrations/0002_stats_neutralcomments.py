# Generated by Django 3.2.3 on 2022-05-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='neutralComments',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]