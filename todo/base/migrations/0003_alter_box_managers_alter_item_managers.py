# Generated by Django 4.0.4 on 2022-04-22 20:01

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_box_additional'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='box',
            managers=[
                ('boxes', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='item',
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
    ]