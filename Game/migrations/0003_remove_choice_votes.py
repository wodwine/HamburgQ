# Generated by Django 2.2.5 on 2019-10-27 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]