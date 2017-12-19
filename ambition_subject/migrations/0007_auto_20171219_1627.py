# Generated by Django 2.0 on 2017-12-19 14:27

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ambition_subject', '0006_auto_20171218_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPkPdExtraSamples',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('extra_csf_samples_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further CSF samples were taken, please add here the exact date and time sample was taken')),
                ('extra_blood_samples_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further blood samples were taken, please add here the exact date and time sample was taken')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='PkPdExtraSamples',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('extra_csf_samples_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further CSF samples were taken, please add here the exact date and time sample was taken')),
                ('extra_blood_samples_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='If any further blood samples were taken, please add here the exact date and time sample was taken')),
            ],
            options={
                'verbose_name': 'PK/PD Extra Samples',
                'verbose_name_plural': 'PK/PD Extra Samples',
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='historicalpkpdcrf',
            old_name='reason_day_one_missed',
            new_name='reason_blood_sample_missed',
        ),
        migrations.RenameField(
            model_name='pkpdcrf',
            old_name='reason_day_one_missed',
            new_name='reason_blood_sample_missed',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='ambisome_dose_time_ended',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='ambisome_dose_time_started',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='any_day_one_sample_missed',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='any_day_seven_sample_missed',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_five_day_one',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_five_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_four_day_one',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_four_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_one_day_one',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_one_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_six_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_three_day_one',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_three_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_two_day_one',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='blood_sample_two_day_seven',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='cd4_cell_count',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='creatine_clearance',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_blood_samples_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='extra_csf_samples_datetime',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_four_time',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_one_time',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_three_time',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_two_time',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='flucytosine_doses_missed',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='haemoglobin',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='magnesium',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='on_art',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='other_medication',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='reason_day_seven_missed',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='second_post_dose_lp',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='second_pre_dose_lp',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='time_fluconazole_dose_given',
        ),
        migrations.RemoveField(
            model_name='historicalpkpdcrf',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='ambisome_dose_time_ended',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='ambisome_dose_time_started',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='any_day_one_sample_missed',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='any_day_seven_sample_missed',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_five_day_one',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_five_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_four_day_one',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_four_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_one_day_one',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_one_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_six_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_three_day_one',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_three_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_two_day_one',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='blood_sample_two_day_seven',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='cd4_cell_count',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='creatine_clearance',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_blood_samples_datetime',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='extra_csf_samples_datetime',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='flucytosine_dose_four_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='flucytosine_dose_one_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='flucytosine_dose_three_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='flucytosine_dose_two_time',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='flucytosine_doses_missed',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='haemoglobin',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='magnesium',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='on_art',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='other_medication',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='reason_day_seven_missed',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='second_post_dose_lp',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='second_pre_dose_lp',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='time_fluconazole_dose_given',
        ),
        migrations.RemoveField(
            model_name='pkpdcrf',
            name='weight',
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='ambisome_ended_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Ambisome infusion stopped'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='ambisome_started_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Ambisome infusion started?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_five_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;5</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_four_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;4</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_one_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;1</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_six_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;6</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_three_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;3</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='blood_sample_two_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;2</u> taken?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='fluconazole_dose_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Fluconazole was swallowed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_four_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;4</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_one_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;1</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_three_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;3</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_two_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;2</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='historicalpkpdcrf',
            name='flucytosine_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any Flucytosine doses missed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='ambisome_ended_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Ambisome infusion stopped'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='ambisome_started_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Ambisome infusion started?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_five_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;5</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_four_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;4</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_one_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;1</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_six_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;6</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_three_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;3</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='blood_sample_two_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time blood <u>SAMPLE&nbsp;2</u> taken?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='fluconazole_dose_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Fluconazole was swallowed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='flucytosine_dose_four_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;4</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='flucytosine_dose_one_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;1</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='flucytosine_dose_three_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;3</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='flucytosine_dose_two_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date and time Flucytosine <u>DOSE&nbsp;2</u> was swallowed?'),
        ),
        migrations.AddField(
            model_name='pkpdcrf',
            name='flucytosine_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Were any Flucytosine doses missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='albumin',
            field=models.IntegerField(blank=True, null=True, verbose_name='Albumin'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='ambisome_dose',
            field=models.IntegerField(blank=True, help_text='Units in mg', null=True, verbose_name='Ambisome dose given'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='fluconazole_dose_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Was the Fluconazole dose missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose',
            field=models.IntegerField(blank=True, help_text='Units in mg', null=True, verbose_name='What was the dose of Flucytosine given?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='full_ambisome_dose_given',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Was the entire Ambisome dose given?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='post_dose_lp',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Is this a post-dose LP?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='pre_dose_lp',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Is this a pre-dose LP?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='time_csf_sample_taken',
            field=models.DateTimeField(blank=True, null=True, verbose_name='What date and time was the CSF sample taken?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='albumin',
            field=models.IntegerField(blank=True, null=True, verbose_name='Albumin'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='ambisome_dose',
            field=models.IntegerField(blank=True, help_text='Units in mg', null=True, verbose_name='Ambisome dose given'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='fluconazole_dose_missed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Was the Fluconazole dose missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose',
            field=models.IntegerField(blank=True, help_text='Units in mg', null=True, verbose_name='What was the dose of Flucytosine given?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='full_ambisome_dose_given',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Was the entire Ambisome dose given?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='post_dose_lp',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Is this a post-dose LP?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='pre_dose_lp',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Is this a pre-dose LP?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='time_csf_sample_taken',
            field=models.DateTimeField(blank=True, null=True, verbose_name='What date and time was the CSF sample taken?'),
        ),
        migrations.AddField(
            model_name='pkpdextrasamples',
            name='pk_pd_crf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambition_subject.PkPdCrf'),
        ),
        migrations.AddField(
            model_name='historicalpkpdextrasamples',
            name='pk_pd_crf',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ambition_subject.PkPdCrf'),
        ),
        migrations.AlterUniqueTogether(
            name='pkpdextrasamples',
            unique_together={('pk_pd_crf', 'extra_csf_samples_datetime', 'extra_blood_samples_datetime')},
        ),
    ]
