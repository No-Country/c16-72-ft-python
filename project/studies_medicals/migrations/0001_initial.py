# Generated by Django 5.0.2 on 2024-02-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudiesMedicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('result', models.FileField(blank=True, null=True, upload_to='estudios_resultados/')),
                ('report', models.TextField(blank=True, null=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeStudieMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
