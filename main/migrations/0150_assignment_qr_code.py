# Generated by Django 4.1.7 on 2025-01-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0149_part_bunnycdn'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='qr_code',
            field=models.ImageField(default='blank-lecture.jpeg', upload_to='qr-codes'),
        ),
    ]
