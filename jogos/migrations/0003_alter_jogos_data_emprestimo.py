# Generated by Django 3.2 on 2021-04-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0002_auto_20210413_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='data_emprestimo',
            field=models.DateTimeField(null=True),
        ),
    ]
