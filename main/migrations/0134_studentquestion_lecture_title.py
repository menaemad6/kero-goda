# Generated by Django 4.1.7 on 2024-09-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0133_alter_chaptermember_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentquestion',
            name='lecture_title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
