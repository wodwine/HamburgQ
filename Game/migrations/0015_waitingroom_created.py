# Generated by Django 2.2.5 on 2019-11-16 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0014_auto_20191112_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitingroom',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
