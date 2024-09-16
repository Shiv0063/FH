# Generated by Django 5.0.4 on 2024-07-31 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_salesentrymodel_lossmargin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 28, 10, 369768)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 28, 10, 354143)),
        ),
        migrations.AlterField(
            model_name='ledgerreportmodel',
            name='LRDate',
            field=models.DateField(default=datetime.date(2024, 7, 31)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 28, 10, 338514)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 28, 10, 354143)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='LossMargin',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='ProfitMargin',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 31, 13, 28, 10, 369768)),
        ),
    ]