# Generated by Django 3.2 on 2021-04-13 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_alter_compras_data_incercao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='data_incercao',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 20, 4, 22, 558777)),
        ),
    ]