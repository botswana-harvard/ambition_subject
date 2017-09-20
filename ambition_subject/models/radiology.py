from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_constants.choices import YES_NO, YES_NO_NA

from ..choices import (ABNORMAL_RESULTS_REASON, BRAIN_IMAGINING_REASON,
                       CXR_TYPE, INFILTRATE_LOCATION)

from .model_mixins import CrfModelMixin
from edc_constants.constants import NOT_APPLICABLE


class Radiology(CrfModelMixin):

    cxr_done = models.CharField(
        verbose_name='Is CXR done',
        choices=YES_NO,
        max_length=5)

    cxr_date = models.DateField(
        verbose_name='If yes, when was CXR done',
        validators=[date_not_future],
        blank=True,
        null=True)

    cxr_type = models.CharField(
        verbose_name='If yes, result',
        blank=False,
        choices=CXR_TYPE,
        default=NOT_APPLICABLE,
        max_length=75,
        null=True)

    infiltrate_location = models.CharField(
        verbose_name='If Infiltrates, specify location',
        blank=False,
        choices=INFILTRATE_LOCATION,
        default=NOT_APPLICABLE,
        max_length=10,
        null=True)

    cxr_description = models.TextField(
        verbose_name='Description/Comments',
        blank=True,
        null=True)

    ct_performed = models.CharField(
        verbose_name='CT/MRI brain scan performed?',
        choices=YES_NO,
        max_length=5)

    ct_performed_date = models.DateTimeField(
        verbose_name='Date CT performed',
        validators=[datetime_not_future],
        editable=True,
        blank=True,
        null=True)

    scanned_with_contrast = models.CharField(
        verbose_name='CT/MRI brain scan performed with contrast?',
        blank=False,
        choices=YES_NO_NA,
        max_length=5,
        null=False)

    brain_imaging_reason = models.CharField(
        verbose_name='Reason for brain imaging',
        blank=False,
        choices=BRAIN_IMAGINING_REASON,
        default=NOT_APPLICABLE,
        max_length=25,
        null=True)

    brain_imaging_reason_other = models.CharField(
        verbose_name='If other, please specify',
        blank=True,
        max_length=50,
        null=True)

    are_results_abnormal = models.CharField(
        blank=False,
        choices=YES_NO_NA,
        null=False,
        max_length=5)

    abnormal_results_reason = models.CharField(
        verbose_name='If results are abnormal, what is the reason?',
        blank=False,
        choices=ABNORMAL_RESULTS_REASON,
        default=NOT_APPLICABLE,
        max_length=50,
        null=True)

    abnormal_results_reason_other = models.CharField(
        verbose_name='If other, please specify reason',
        blank=True,
        max_length=50,
        null=True)

    infarcts_location = models.CharField(
        verbose_name='If results are abnormal because of Infarcts, what is '
                     'the location?',
        blank=True,
        max_length=50,
        null=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Radiology'
