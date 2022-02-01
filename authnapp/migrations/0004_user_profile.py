# Generated by Django 3.2.11 on 2022-02-01 17:43

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0003_default_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 3, 17, 43, 16, 425222, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]