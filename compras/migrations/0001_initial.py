# Generated by Django 3.2 on 2021-04-13 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=20)),
                ('quantidade', models.CharField(max_length=20)),
                ('data_incercao', models.DateTimeField(default=datetime.datetime(2021, 4, 13, 18, 45, 15, 614931))),
            ],
        ),
    ]
