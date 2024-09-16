# Generated by Django 5.0.4 on 2024-06-02 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 40, 43, 174036)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 40, 43, 168037)),
        ),
        migrations.AlterField(
            model_name='ledgerreportmodel',
            name='LRDate',
            field=models.DateField(default=datetime.date(2024, 6, 2)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 40, 43, 154039)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 40, 43, 165036)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 40, 43, 175037)),
        ),
    ]