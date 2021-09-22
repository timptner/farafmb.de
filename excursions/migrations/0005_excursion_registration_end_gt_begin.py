# Generated by Django 3.2.4 on 2021-09-22 20:20

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('excursions', '0004_alter_excursion_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='excursion',
            constraint=models.CheckConstraint(check=models.Q(('registration_begins_at__lt', django.db.models.expressions.F('registration_ends_at'))), name='registration_end_gt_begin'),
        ),
    ]
