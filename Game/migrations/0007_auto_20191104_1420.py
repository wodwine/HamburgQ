# Generated by Django 2.2.5 on 2019-11-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0006_auto_20191104_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.CharField(max_length=20),
        ),
    ]