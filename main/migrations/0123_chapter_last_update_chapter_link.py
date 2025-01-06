# Generated by Django 4.1.7 on 2024-08-30 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0122_studentpartobject_pdf_file_pages_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='chapter',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
