from django.db import models

from edc_base.model_managers import HistoricalRecords

from .model_mixins import CrfModelMixin


class ClinicNote(CrfModelMixin):

    subjective = models.TextField(
        max_length=1000)

    vital_signs = models.TextField(
        max_length=100)

    cvs = models.TextField(
        max_length=100)

    resp = models.TextField(
        max_length=100)

    neuro = models.TextField(
        max_length=100)

    assessment = models.TextField(
        max_length=100)

    plan = models.TextField(
        max_length=1000)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        pass
