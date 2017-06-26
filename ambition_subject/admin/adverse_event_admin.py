from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventForm
from ..models import AdverseEvent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEvent, site=ambition_subject_admin)
class AdverseEventAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm

    radio_fields = {
        'report_type': admin.VERTICAL,
        'ae_severity_grade': admin.VERTICAL,
        'ae_study_relation_possibility': admin.VERTICAL,
        'ambisome_relation': admin.VERTICAL,
        'fluconazole_relation': admin.VERTICAL,
        'amphotericin_b_relation': admin.VERTICAL,
        'ae_cause': admin.VERTICAL,
        'ae_cm_recurrence': admin.VERTICAL,
        'is_sa_event': admin.VERTICAL,
        'sae_possibility': admin.VERTICAL,
        'susar_possility': admin.VERTICAL}

    fieldsets = (
        ('Initial Report', {
            'fields': (
                'subject_visit',
                'report_type',
                'ae_description',
                'ae_start_date',
                'ae_severity_grade',
                'regimen',
                'ae_study_relation_possibility',
                'possiblity_detail',
                'ambisome_relation',
                'fluconazole_relation',
                'amphotericin_b_relation',
                'details_last_study_drug',
                'med_administered_datetime',
                'implicated_med',
                'implicated_med_dose',
                'implicated_med_route',
                'ae_cause',
                'ae_cause_other',
                'ae_treatment',
                'ae_cm_recurrence',
                'is_sa_event',
                'sae_possibility',
                'susar_possility')},
         ),
        audit_fieldset_tuple
    )
