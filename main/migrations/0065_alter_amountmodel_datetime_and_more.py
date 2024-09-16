# Generated by Django 5.0.4 on 2024-06-05 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 20, 27, 45, 951601)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 20, 27, 45, 951601)),
        ),
        migrations.AlterField(
            model_name='ledgerreportmodel',
            name='LRDate',
            field=models.DateField(default=datetime.date(2024, 6, 5)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 20, 27, 45, 935942)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 20, 27, 45, 951601)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 20, 27, 45, 951601)),
        ),
    ]
