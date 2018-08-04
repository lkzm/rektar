# Generated by Django 2.0.7 on 2018-08-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=200)),
                ('previous', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='options',
            field=models.ManyToManyField(to='nav.MenuOption'),
        ),
    ]
