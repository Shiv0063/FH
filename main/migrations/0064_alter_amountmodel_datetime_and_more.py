# Generated by Django 5.0.4 on 2024-06-04 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 17, 40, 50, 977790)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 17, 40, 50, 977790)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 17, 40, 50, 962260)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 17, 40, 50, 962260)),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='BarcodeImg',
            field=models.FileField(blank=True, upload_to='Barcode/'),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 17, 40, 50, 977790)),
        ),
    ]
