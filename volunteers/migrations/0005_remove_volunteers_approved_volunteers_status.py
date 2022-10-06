# Generated by Django 4.1 on 2022-09-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_alter_volunteers_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteers',
            name='approved',
        ),
        migrations.AddField(
            model_name='volunteers',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
