# Generated by Django 4.2.1 on 2023-05-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinger', '0002_pings_host_pings_status_alter_pings_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='pings',
            name='turbine_name',
            field=models.CharField(default='X01YCA01UH002', max_length=20),
        ),
        migrations.AddField(
            model_name='pings',
            name='windfarm_name',
            field=models.CharField(default='HOW01-GEN', max_length=20),
        ),
    ]