# Generated by Django 4.0.1 on 2022-02-21 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikedItem',
        ),
    ]
