# Generated by Django 5.0.4 on 2024-04-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productmodel_hsncode'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='MRP',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
