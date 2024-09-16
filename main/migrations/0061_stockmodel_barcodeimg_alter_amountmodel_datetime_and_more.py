# Generated by Django 5.0.4 on 2024-06-04 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='BarcodeImg',
            field=models.ImageField(blank=True, upload_to='Barcode/'),
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 14, 56, 892333)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 14, 56, 892333)),
        ),
        migrations.AlterField(
            model_name='ledgerreportmodel',
            name='LRDate',
            field=models.DateField(default=datetime.date(2024, 6, 4)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 14, 56, 876695)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 14, 56, 876695)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 11, 14, 56, 892333)),
        ),
    ]
