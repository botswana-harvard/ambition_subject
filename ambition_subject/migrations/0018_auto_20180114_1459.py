# Generated by Django 2.0.1 on 2018-01-14 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0017_auto_20180114_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsubjectrequisition',
            name='panel_name',
        ),
        migrations.RemoveField(
            model_name='subjectrequisition',
            name='panel_name',
        ),
    ]