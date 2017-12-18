# Generated by Django 2.0 on 2017-12-17 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0003_auto_20171212_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deathreporttmgone',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='deathreporttmgtwo',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreport',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgone',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgone',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgtwo',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgtwo',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalprotocoldeviationviolation',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalrecurrencesymptom',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalrecurrencesymptom',
            name='subject_visit',
        ),
        migrations.RemoveField(
            model_name='historicalstudyterminationconclusion',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalsubjectoffstudy',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='ProtocolDeviationViolation',
        ),
        migrations.RemoveField(
            model_name='recurrencesymptom',
            name='antibiotic_treatment',
        ),
        migrations.RemoveField(
            model_name='recurrencesymptom',
            name='meningitis_symptom',
        ),
        migrations.RemoveField(
            model_name='recurrencesymptom',
            name='neurological',
        ),
        migrations.RemoveField(
            model_name='recurrencesymptom',
            name='subject_visit',
        ),
        migrations.DeleteModel(
            name='StudyTerminationConclusion',
        ),
        migrations.DeleteModel(
            name='SubjectOffstudy',
        ),
        migrations.RenameField(
            model_name='historicalmedicalexpenses',
            old_name='proxy_he_spend',
            new_name='someone_spent_last_4wks',
        ),
        migrations.RenameField(
            model_name='historicalmedicalexpenses',
            old_name='personal_he_spend',
            new_name='subject_spent_last_4wks',
        ),
        migrations.RenameField(
            model_name='historicalmedicalexpenses',
            old_name='he_spend_last_4weeks',
            new_name='total_spent_last_4wks',
        ),
        migrations.RenameField(
            model_name='medicalexpenses',
            old_name='proxy_he_spend',
            new_name='someone_spent_last_4wks',
        ),
        migrations.RenameField(
            model_name='medicalexpenses',
            old_name='personal_he_spend',
            new_name='subject_spent_last_4wks',
        ),
        migrations.RenameField(
            model_name='medicalexpenses',
            old_name='he_spend_last_4weeks',
            new_name='total_spent_last_4wks',
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='alt_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='cd4_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='creatinine_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='haemoglobin_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='magnesium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='neutrophil_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='platelets_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='potassium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='sodium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='urea_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='wbc_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='alt_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='cd4_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='creatinine_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='haemoglobin_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='magnesium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='neutrophil_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='platelets_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='potassium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='sodium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='urea_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='wbc_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], default='N/A', max_length=6, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicallumbarpuncturecsf',
            name='csf_culture',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('awaiting_results', 'Awaiting results'), ('not_done', 'Not done')], default='awaiting_results', help_text='Complete after getting the results.', max_length=18, verbose_name='Other organism (non-Cryptococcus)'),
        ),
        migrations.AlterField(
            model_name='historicallumbarpuncturecsf',
            name='differential_lymphocyte_unit',
            field=models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='historicallumbarpuncturecsf',
            name='differential_neutrophil_unit',
            field=models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='historicalmicrobiology',
            name='sputum_result_genexpert',
            field=models.CharField(choices=[('mtb_detected_rif_resistance_detected', 'MTB DETECTED & Rif Resistance DETECTED'), ('mtb_detected_rif_resistance_not_detected', 'MTB DETECTED & Rif Resistance NOT detected'), ('mtb_detected_rif_resistance_indeterminate', 'MTB DETECTED & Rif Resistance INDETERMINATE'), ('mtb_not_detected', 'MTB NOT detected'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Gene-Xpert results'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='last_dose',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='If no tablets taken this month, how many months since the last dose taken?'),
        ),
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='tablets_missed',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)], verbose_name='If not adherent, how many tablets missed in the last month?'),
        ),
        migrations.AlterField(
            model_name='historicalprnmodel',
            name='cd4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='CD4?'),
        ),
        migrations.AlterField(
            model_name='historicalprnmodel',
            name='chemistry',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Chemistry?'),
        ),
        migrations.AlterField(
            model_name='historicalprnmodel',
            name='fbc',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='FBC?'),
        ),
        migrations.AlterField(
            model_name='historicalprnmodel',
            name='viral_load',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Viral Load?'),
        ),
        migrations.AlterField(
            model_name='lumbarpuncturecsf',
            name='csf_culture',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('awaiting_results', 'Awaiting results'), ('not_done', 'Not done')], default='awaiting_results', help_text='Complete after getting the results.', max_length=18, verbose_name='Other organism (non-Cryptococcus)'),
        ),
        migrations.AlterField(
            model_name='lumbarpuncturecsf',
            name='differential_lymphocyte_unit',
            field=models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='lumbarpuncturecsf',
            name='differential_neutrophil_unit',
            field=models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='microbiology',
            name='sputum_result_genexpert',
            field=models.CharField(choices=[('mtb_detected_rif_resistance_detected', 'MTB DETECTED & Rif Resistance DETECTED'), ('mtb_detected_rif_resistance_not_detected', 'MTB DETECTED & Rif Resistance NOT detected'), ('mtb_detected_rif_resistance_indeterminate', 'MTB DETECTED & Rif Resistance INDETERMINATE'), ('mtb_not_detected', 'MTB NOT detected'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Gene-Xpert results'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='last_dose',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='If no tablets taken this month, how many months since the last dose taken?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='neurological',
            field=models.ManyToManyField(blank=True, to='ambition_ae.Neurological'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='tablets_missed',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)], verbose_name='If not adherent, how many tablets missed in the last month?'),
        ),
        migrations.AlterField(
            model_name='prnmodel',
            name='cd4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='CD4?'),
        ),
        migrations.AlterField(
            model_name='prnmodel',
            name='chemistry',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Chemistry?'),
        ),
        migrations.AlterField(
            model_name='prnmodel',
            name='fbc',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='FBC?'),
        ),
        migrations.AlterField(
            model_name='prnmodel',
            name='viral_load',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Viral Load?'),
        ),
        migrations.DeleteModel(
            name='AntibioticTreatment',
        ),
        migrations.DeleteModel(
            name='DeathReport',
        ),
        migrations.DeleteModel(
            name='DeathReportTmgOne',
        ),
        migrations.DeleteModel(
            name='DeathReportTmgTwo',
        ),
        migrations.DeleteModel(
            name='HistoricalDeathReport',
        ),
        migrations.DeleteModel(
            name='HistoricalDeathReportTmgOne',
        ),
        migrations.DeleteModel(
            name='HistoricalDeathReportTmgTwo',
        ),
        migrations.DeleteModel(
            name='HistoricalProtocolDeviationViolation',
        ),
        migrations.DeleteModel(
            name='HistoricalRecurrenceSymptom',
        ),
        migrations.DeleteModel(
            name='HistoricalStudyTerminationConclusion',
        ),
        migrations.DeleteModel(
            name='HistoricalSubjectOffstudy',
        ),
        migrations.DeleteModel(
            name='MeningitisSymptom',
        ),
        migrations.DeleteModel(
            name='Neurological',
        ),
        migrations.DeleteModel(
            name='RecurrenceSymptom',
        ),
    ]