# Generated by Django 2.2.5 on 2019-11-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0013_auto_20191112_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='current_question',
            field=models.IntegerField(default=0),
        ),
    ]