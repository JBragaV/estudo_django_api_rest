# Generated by Django 3.2 on 2021-04-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispensa', '0002_alter_dispensa_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispensa',
            name='quantidade',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
