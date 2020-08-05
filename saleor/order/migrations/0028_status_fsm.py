# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("order", "0027_auto_20180108_0814")]

    operations = [
        migrations.AlterField(
            model_name="deliverygroup",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "Processing"),
                    ("cancelled", "Cancelled"),
                    ("shipped", "Shipped"),
                ],
                default="new",
                max_length=32,
                verbose_name="shipment status",
            ),
        )
    ]
