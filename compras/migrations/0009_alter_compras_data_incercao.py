# Generated by Django 3.2 on 2021-05-05 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_alter_compras_data_incercao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='data_incercao',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 22, 44, 12, 401379)),
        ),
    ]
