# Generated by Django A.B on YYYY-MM-DD HH:MM
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0007_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='OnlineCoupons',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
