# Generated by Django 4.0.6 on 2022-07-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0002_helper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
    ]
