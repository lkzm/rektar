# Generated by Django 2.0.7 on 2018-07-16 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0008_auto_20180716_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adventure',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='adventure',
            name='completed',
        ),
        migrations.AddField(
            model_name='adventure',
            name='date_finished',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='adventure',
            name='date_started',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='adventure',
            name='status',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 7, 16, 23, 18, 40, 960514)),
        ),
    ]
