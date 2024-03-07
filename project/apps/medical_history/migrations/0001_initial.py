# Generated by Django 5.0.2 on 2024-03-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('chronic_diseases', models.TextField(blank=True, null=True)),
                ('family_history', models.TextField(blank=True, null=True)),
                ('surgeries', models.TextField(blank=True, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('medications', models.TextField(blank=True, null=True)),
                ('vaccines', models.TextField(blank=True, null=True)),
                ('habits', models.TextField(blank=True, null=True)),
                ('observations', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
