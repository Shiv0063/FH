# Generated by Django 5.0.4 on 2024-05-31 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_remove_salesstockmodel_payableamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesentrymodel',
            name='status',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 159451)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 152449)),
        ),
        migrations.AlterField(
            model_name='ledgerreportmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 161449)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 139453)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 149452)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 21, 19, 20, 160449)),
        ),
    ]
