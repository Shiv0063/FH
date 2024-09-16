# Generated by Django 5.0.4 on 2024-06-13 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_salesentrymodel_vendorpartyname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesentrymodel',
            name='VendorPartyName',
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 22, 28, 57, 501698)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 22, 28, 57, 501698)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 22, 28, 57, 489346)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 22, 28, 57, 501698)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 22, 28, 57, 517322)),
        ),
    ]
