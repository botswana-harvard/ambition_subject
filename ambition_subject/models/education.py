from django.db import models
from edc_base.model_managers import HistoricalRecords
from ..managers import CurrentSiteManager
from edc_constants.choices import YES_NO
from edc_visit_tracking.managers import CrfModelManager

from .model_mixins import CrfModelMixin, EducationModelMixin


class Education(EducationModelMixin, CrfModelMixin):

    household_head = models.CharField(
        verbose_name='Are you the person who earns the highest income?',
        max_length=5,
        choices=YES_NO,
        help_text=('If NO, please complete the form "Health Economics: '
                   'Education (Person who earns the highest income)" on behalf of the '
                   'Person who earns the highest income.'))

    on_site = CurrentSiteManager()

    objects = CrfModelManager()

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Health Economics: Education'
        verbose_name_plural = 'Health Economics: Education'
