# Generated by Django 4.0.6 on 2022-09-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoggerDebug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=2000, verbose_name='log')),
            ],
            options={
                'verbose_name': 'log - debug',
                'verbose_name_plural': 'logs - debug',
            },
        ),
        migrations.CreateModel(
            name='LoggerProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=2000, verbose_name='log')),
            ],
            options={
                'verbose_name': 'log - production',
                'verbose_name_plural': 'logs - production',
            },
        ),
    ]
