# Generated by Django 5.0.2 on 2024-03-18 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('cpf', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('rg', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[(None, 'Selecione um sexo'), ('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Outro')], default='', max_length=100)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
    ]
