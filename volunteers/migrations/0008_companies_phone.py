# Generated by Django 4.1 on 2022-09-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0007_companies_policy_couponsbought_comment_discardlost'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]