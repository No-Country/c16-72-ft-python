# Generated by Django 5.0.2 on 2024-03-05 03:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical_history', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='medical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medic_historys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
