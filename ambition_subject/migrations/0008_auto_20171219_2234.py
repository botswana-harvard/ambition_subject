# Generated by Django 2.0 on 2017-12-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0007_auto_20171219_1627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disenrollment',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.DeleteModel(
            name='EnrollmentW10',
        ),
        migrations.RemoveField(
            model_name='historicaldisenrollment',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalenrollment',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalenrollmentw10',
            name='history_user',
        ),
        migrations.AddField(
            model_name='historicalsubjectconsent',
            name='updates_versions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subjectconsent',
            name='updates_versions',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='HistoricalDisenrollment',
        ),
        migrations.DeleteModel(
            name='HistoricalEnrollment',
        ),
        migrations.DeleteModel(
            name='HistoricalEnrollmentW10',
        ),
    ]
