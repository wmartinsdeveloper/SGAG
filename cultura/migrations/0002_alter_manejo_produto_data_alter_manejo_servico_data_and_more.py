# Generated by Django 5.1.1 on 2024-11-05 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manejo_produto',
            name='data',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='manejo_servico',
            name='data',
            field=models.DateField(blank=True),
        ),
        migrations.CreateModel(
            name='plantio',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('datainicio', models.DateField(blank=True)),
                ('datafim', models.DateField(blank=True)),
                ('medidaarea', models.CharField(max_length=100)),
                ('descricao', models.TextField(default='')),
                ('quantidadeplanta', models.IntegerField()),
                ('manejo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plantio_manejo', to='cultura.manejo')),
            ],
        ),
        migrations.CreateModel(
            name='producao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.DateField(blank=True)),
                ('quantidade', models.IntegerField()),
                ('unidadeproducao', models.CharField(max_length=50)),
                ('precovenda', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('plantio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plantio', to='cultura.plantio')),
            ],
        ),
    ]
