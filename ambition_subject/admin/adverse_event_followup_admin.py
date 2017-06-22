from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventFollowUpForm
from ..models import AdverseEventFollowUp
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEventFollowUp, site=ambition_subject_admin)
class AdverseEventFollowUpAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventFollowUpForm

    radio_fields = {
        'outcome': admin.VERTICAL}

    fieldsets = (
        ('Clinical Assessment', {
            'fields': (
                'subject_visit',
                'outcome',
                'outcome_date',
                'relevant_history')},
         ),
        audit_fieldset_tuple
    )