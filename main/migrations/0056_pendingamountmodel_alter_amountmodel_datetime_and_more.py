# Generated by Django 5.0.4 on 2024-06-01 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_alter_amountmodel_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingAmountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('PartyName', models.CharField(blank=True, max_length=100, null=True)),
                ('Number', models.CharField(blank=True, max_length=100, null=True)),
                ('CeditedAmount', models.CharField(blank=True, max_length=100, null=True)),
                ('PayableAmount', models.CharField(blank=True, max_length=100, null=True)),
                ('TypeofPayment', models.CharField(blank=True, max_length=100, null=True)),
                ('TransactionID', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='amountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 12, 47, 28, 604159)),
        ),
        migrations.AlterField(
            model_name='expanseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 12, 47, 28, 599158)),
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 12, 47, 28, 586159)),
        ),
        migrations.AlterField(
            model_name='salesentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 12, 47, 28, 595157)),
        ),
        migrations.AlterField(
            model_name='useramountmodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 1, 12, 47, 28, 605158)),
        ),
    ]
