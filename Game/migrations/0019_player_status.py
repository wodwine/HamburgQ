# Generated by Django 2.2.5 on 2019-11-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0018_auto_20191119_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.CharField(default='Player', max_length=20),
        ),
    ]
