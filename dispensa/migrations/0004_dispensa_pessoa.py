# Generated by Django 3.2 on 2021-04-13 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('dispensa', '0003_alter_dispensa_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispensa',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoas'),
        ),
    ]
