# Generated by Django 4.1 on 2022-08-29 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_alter_volunteers_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='volunteers.branch'),
        ),
    ]