# Generated by Django 3.2 on 2021-04-09 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(default='Produto sem nome', max_length=30)),
                ('quantidade', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['nome_produto'],
            },
        ),
    ]
