# Generated by Django 3.2 on 2021-04-13 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('jogos', '0003_alter_jogos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoas'),
        ),
    ]