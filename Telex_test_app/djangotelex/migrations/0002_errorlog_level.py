# Generated by Django 5.1.5 on 2025-02-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangotelex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorlog',
            name='level',
            field=models.CharField(choices=[('info', 'Info'), ('warning', 'Warning'), ('error', 'Error'), ('critical', 'Critical')], default='error', max_length=10),
        ),
    ]
