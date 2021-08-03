# Generated by Django 3.2.5 on 2021-07-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta_lei', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCodigo', models.CharField(max_length=150, verbose_name='Nome do código')),
                ('ehDividido', models.CharField(max_length=1, verbose_name='É dividido')),
            ],
        ),
    ]
