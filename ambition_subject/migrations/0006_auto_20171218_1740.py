# Generated by Django 2.0 on 2017-12-18 15:40

from django.db import migrations, models
import edc_base.model_validators.date


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0005_auto_20171218_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_blood_samples_date',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_blood_samples_time',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_csf_samples_date',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_csf_samples_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_blood_samples_date',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_blood_samples_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_csf_samples_date',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_csf_samples_time',
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='extra_blood_samples_datetime',
            field=models.DateTimeField(null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further blood samples were taken, please add here the exact date and time sample was taken'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='extra_csf_samples_datetime',
            field=models.DateTimeField(null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further CSF samples were taken, please add here the exact date and time sample was taken'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='extra_blood_samples_datetime',
            field=models.DateTimeField(null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further blood samples were taken, please add here the exact date and time sample was taken'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='extra_csf_samples_datetime',
            field=models.DateTimeField(null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further CSF samples were taken, please add here the exact date and time sample was taken'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='any_day_one_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='any_day_seven_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_missed',
            field=models.CharField(blank=True, choices=[('dose_1', 'Dose 1'), ('dose_2', 'Dose 2'), ('dose_3', 'Dose 3'), ('dose_4', 'Dose 4')], max_length=5, null=True, verbose_name='Which dose(s) was/were missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='reason_fluconazole_dose_missed',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Why was the Fluconazole dose missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='time_csf_sample_taken',
            field=models.TimeField(max_length=5, null=True, verbose_name='What time was the CSF sample taken?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='any_day_one_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='any_day_seven_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose_missed',
            field=models.CharField(blank=True, choices=[('dose_1', 'Dose 1'), ('dose_2', 'Dose 2'), ('dose_3', 'Dose 3'), ('dose_4', 'Dose 4')], max_length=5, null=True, verbose_name='Which dose(s) was/were missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='reason_fluconazole_dose_missed',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Why was the Fluconazole dose missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='time_csf_sample_taken',
            field=models.TimeField(max_length=5, null=True, verbose_name='What time was the CSF sample taken?'),
        ),
    ]