# Generated by Django 3.2 on 2021-05-05 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_alter_compras_data_incercao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='data_incercao',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 22, 40, 17, 543515)),
        ),
    ]