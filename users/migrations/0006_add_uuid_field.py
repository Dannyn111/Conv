from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='OnlineCoupons',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
