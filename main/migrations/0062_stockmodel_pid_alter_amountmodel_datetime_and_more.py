# Generated by Django 5.0.4 on 2024-06-04 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_stockmodel_barcodeimg_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='PID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 25, 10, 317809)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 25, 10, 302185)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 25, 10, 286561)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 25, 10, 302185)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 25, 10, 317809)),
        ),
    ]
