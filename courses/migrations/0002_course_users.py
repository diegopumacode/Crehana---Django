# Generated by Django 3.1.7 on 2021-02-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.IntegerField(default=1),
        ),
    ]
