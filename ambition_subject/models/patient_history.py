from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_fields import OtherCharField, IsDateEstimatedField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from ..choices import FIRST_LINE_REGIMEN, FIRST_ARV_REGIMEN, TB_SITE
from ..choices import INFECTION, ECOG_SCORE, SECOND_ARV_REGIMEN
from .list_models import Medication, Neurological
from .list_models import Symptom
from .model_mixins import CrfModelMixin, MedicalExpensesMixin


class PreviousOpportunisticInfectionManager(models.Manager):

    def get_by_natural_key(self, previous_non_tb_oi, previous_non_tb_oi_date,
                           subject_identifier, visit_schedule_name,
                           schedule_name, visit_code):
        return self.get(
            previous_non_tb_oi=previous_non_tb_oi,
            previous_non_tb_oi_date=previous_non_tb_oi_date,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class PatientHistory(MedicalExpensesMixin, CrfModelMixin):

    symptom = models.ManyToManyField(
        Symptom,
        blank=True,
        related_name='symptoms',
        verbose_name='What are your current symptoms?')

    headache_duration = models.IntegerField(
        verbose_name='If headache, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    visual_loss_duration = models.IntegerField(
        verbose_name='If visual loss, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    tb_history = models.CharField(
        verbose_name='Previous medical history of Tuberculosis?',
        max_length=5,
        choices=YES_NO)

    tb_site = models.CharField(
        verbose_name='If Yes, site of TB?',
        max_length=15,
        choices=TB_SITE,
        default=NOT_APPLICABLE)

    tb_treatment = models.CharField(
        verbose_name='Are you currently taking TB treatment?',
        max_length=5,
        choices=YES_NO)

    taking_rifampicin = models.CharField(
        verbose_name='If yes, are you currently also taking Rifampicin?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    rifampicin_started_date = models.DateField(
        verbose_name='If yes, when did you first start taking Rifampicin?',
        validators=[date_not_future],
        null=True,
        blank=True)

    new_hiv_diagnosis = models.CharField(
        verbose_name='Is this a new HIV diagnosis?',
        max_length=5,
        choices=YES_NO)

    taking_arv = models.CharField(
        verbose_name='If No, Already taking ARVs?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    arv_date = models.DateField(
        verbose_name='If yes, date ARVs were started.',
        validators=[date_not_future],
        null=True,
        blank=True)

    first_arv_regimen = models.CharField(
        verbose_name='Drug used in first line arv regimen',
        max_length=50,
        choices=FIRST_ARV_REGIMEN,
        default=NOT_APPLICABLE)

    first_arv_regimen_other = OtherCharField()

    second_arv_regimen = models.CharField(
        verbose_name='Second line arv regimen',
        max_length=50,
        choices=SECOND_ARV_REGIMEN,
        default=NOT_APPLICABLE)

    second_arv_regimen_other = OtherCharField()

    first_line_choice = models.CharField(
        verbose_name='If first line:',
        max_length=5,
        choices=FIRST_LINE_REGIMEN,
        default=NOT_APPLICABLE)

    patient_adherence = models.CharField(
        verbose_name='Is the patient reportedly adherent?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    last_dose = models.IntegerField(
        verbose_name='If no, how many months since the last dose '
        'was taken?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    days_missed = models.IntegerField(
        verbose_name='If no, how many days of treatment missed this month?',
        validators=[MinValueValidator(0), MaxValueValidator(31)],
        null=True,
        blank=True)

    last_viral_load = models.DecimalField(
        verbose_name='Last Viral Load, if known?',
        decimal_places=3,
        max_digits=10,
        null=True,
        blank=True,
        help_text='copies/mL')

    viral_load_date = models.DateField(
        verbose_name='Viral load date',
        validators=[date_not_future],
        null=True,
        blank=True
    )

    vl_date_estimated = IsDateEstimatedField(
        blank=True,
        null=True,
        verbose_name=("Is the subject's viral load date estimated?"))

    last_cd4 = models.IntegerField(
        verbose_name='Last CD4, if known?',
        validators=[MinValueValidator(1), MaxValueValidator(2500)],
        null=True,
        blank=True)

    cd4_date = models.DateField(
        verbose_name='CD4 date',
        validators=[date_not_future],
        null=True,
        blank=True
    )

    cd4_date_estimated = IsDateEstimatedField(
        verbose_name=("Is the subject's CD4 date estimated?"),
        blank=True,
        null=True)

    temp = models.DecimalField(
        verbose_name='Temperature:',
        validators=[MinValueValidator(30), MaxValueValidator(45)],
        decimal_places=1,
        max_digits=3,
        help_text='in degrees Celcius')

    heart_rate = models.IntegerField(
        verbose_name='Heart Rate:',
        validators=[MinValueValidator(30), MaxValueValidator(200)],
        help_text='bpm')

    sys_blood_pressure = models.IntegerField(
        verbose_name='Blood Pressure: systolic',
        validators=[MinValueValidator(50), MaxValueValidator(220)],
        help_text='in mm. format SYS, e.g. 120')

    dia_blood_pressure = models.IntegerField(
        verbose_name='Blood Pressure: diastolic',
        validators=[MinValueValidator(20), MaxValueValidator(150)],
        help_text='in Hg. format DIA, e.g. 80')

    respiratory_rate = models.IntegerField(
        verbose_name='Respiratory Rate:',
        validators=[MinValueValidator(6), MaxValueValidator(50)],
        help_text='breaths/min')

    weight = models.DecimalField(
        verbose_name='Weight:',
        validators=[MinValueValidator(20), MaxValueValidator(150)],
        decimal_places=1,
        max_digits=4,
        help_text='Kg')

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score:',
        validators=[MinValueValidator(3), MaxValueValidator(15)],
        help_text='/15')

    neurological = models.ManyToManyField(
        Neurological,
        blank=True)

    neurological_other = OtherCharField(
        verbose_name='If other CN palsy, specify',
        max_length=250,
        blank=True,
        null=True)

    focal_neurologic_deficit = models.TextField(
        verbose_name='If focal neurologic deficit chosen, please '
        'specify details:',
        null=True,
        blank=True)

    visual_acuity_day = models.DateField(
        verbose_name='Study day visual acuity recorded?',
        validators=[date_not_future],
        null=True,
        blank=True)

    left_acuity = models.DecimalField(
        verbose_name='Visual acuity Left eye:',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    right_acuity = models.DecimalField(
        verbose_name='Visual Acuity Right eye',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    ecog_score = models.CharField(
        verbose_name='ECOG Disability score',
        max_length=15,
        choices=ECOG_SCORE)

    ecog_score_value = models.CharField(
        verbose_name='ECOG Score',
        max_length=15,
        choices=ECOG_SCORE)

    lung_exam = models.CharField(
        verbose_name='Abnormal lung exam:',
        max_length=5,
        choices=YES_NO)

    cryptococcal_lesions = models.CharField(
        verbose_name='Cryptococcal related skin lesions:',
        max_length=5,
        choices=YES_NO)

    specify_medications = models.ManyToManyField(
        Medication,
        blank=True)

    specify_medications_other = models.TextField(
        verbose_name='...if "Other", specify',
        max_length=150,
        blank=True,
        null=True)

    household_head = models.CharField(
        verbose_name='Are you head of the household?',
        max_length=5,
        choices=YES_NO)

    profession = models.CharField(
        verbose_name='What is your profession?',
        max_length=25,
        blank=True,
        null=True)

    education_years = models.IntegerField(
        verbose_name='How many years of education did you complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    education_certificate = models.CharField(
        verbose_name='What is your highest education certificate?',
        max_length=25,
        blank=True,
        null=True)

    elementary_school = models.CharField(
        verbose_name='Did you go to elementary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    elementary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    secondary_school = models.CharField(
        verbose_name='Did you go to secondary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    secondary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    higher_education = models.CharField(
        verbose_name='Did you go to higher education?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    higher_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_profession = models.CharField(
        verbose_name='What is the head of household profession?',
        max_length=25,
        blank=True,
        null=True)

    head_education_years = models.IntegerField(
        verbose_name='How many years of education did '
        'head of houesehold complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_education_certificate = models.CharField(
        verbose_name='What is the head of household highest education '
        'certificate?',
        max_length=25,
        blank=True,
        null=True)

    head_elementary = models.CharField(
        verbose_name='Did the head of household go to elementary '
        'school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    head_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_secondary = models.CharField(
        verbose_name='Did head of household go to secondary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    head_secondary_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_higher_education = models.CharField(
        verbose_name='Did head of household go to higher education?',
        max_length=5,
        choices=YES_NO,
        blank=True,
        null=True)

    head_higher_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    previous_oi = models.CharField(
        verbose_name='Previous opportunistic infection other than TB?',
        max_length=5,
        choices=YES_NO)

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Patients History'


class PreviousOpportunisticInfection(BaseUuidModel):

    patient_history = models.ForeignKey(PatientHistory)

    previous_non_tb_oi = models.CharField(
        verbose_name='If other previous opportunistic infection, please specify.',
        max_length=25,
        choices=INFECTION,
        blank=True)

    previous_non_tb_oi_other = models.CharField(
        verbose_name='If other, please specify',
        null=True,
        blank=True,
        max_length=50)

    previous_non_tb_oi_date = models.DateField(
        verbose_name='If infection, what was the date?',
        validators=[date_not_future],
        null=True,
        blank=True)

    objects = PreviousOpportunisticInfectionManager()

    def natural_key(self):
        return (
            (self.previous_non_tb_oi, self.previous_non_tb_oi_date)
            + self.patient_history.natural_key())
    natural_key.dependencies = ['ambition_subject.patienthistory']

    class Meta:
        verbose_name_plural = 'Previous Opportunistic Infection'
        unique_together = (
            'patient_history', 'previous_non_tb_oi', 'previous_non_tb_oi_date')
