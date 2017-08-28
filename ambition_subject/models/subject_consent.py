from django.apps import apps as django_apps
from django.db import models
from django.core.validators import RegexValidator
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField)
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager


from ..choices import ID_TYPE
from .model_mixins import SearchSlugModelMixin


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
        ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    first_name = FirstnameField()

    last_name = LastnameField(
        verbose_name="Last name",
    )

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.')), ],
    )

    screening_identifier = models.CharField(
        verbose_name='Screening Identifier',
        max_length=50)

    is_signed = models.BooleanField(default=False, editable=False)

    may_store_genetic_samples = models.CharField(
        verbose_name=('Does the subject agree that a portion of the blood sample '
                      'that is taken be stored for genetic analysis?'),
        max_length=25,
        choices=YES_NO)

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=ID_TYPE)

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.registration_identifier = self.screening_identifier
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.study_site = edc_protocol_app_config.site_code
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    @property
    def registration_unique_field(self):
        return 'subject_identifier'

    class Meta(ConsentModelMixin.Meta):
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('subject_identifier', 'screening_identifier'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)
