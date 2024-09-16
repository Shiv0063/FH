# Generated by Django 5.0.4 on 2024-06-01 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgerreportmodel',
            name='DateTime',
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 40, 42, 410602)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 40, 42, 402607)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 40, 42, 387609)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 40, 42, 398606)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 11, 40, 42, 411599)),
        ),
    ]
