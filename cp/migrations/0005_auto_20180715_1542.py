# Generated by Django 2.0.7 on 2018-07-15 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0004_auto_20180715_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='sheets',
        ),
        migrations.AddField(
            model_name='sheet',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cp.Character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cp.Description'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='url',
            field=models.URLField(),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
