# Generated by Django 4.1.7 on 2023-10-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_part_type_alter_studentpartobject_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
