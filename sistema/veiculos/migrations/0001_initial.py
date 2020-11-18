# Generated by Django 3.1.3 on 2020-11-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='veiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ano_fabricacao', models.IntegerField()),
                ('modelo_fabricacao', models.IntegerField()),
                ('combustivel', models.SmallIntegerField(choices=[(1, 'ETANOL'), (2, 'FLEX'), (3, 'gasolina')])),
            ],
        ),
    ]
