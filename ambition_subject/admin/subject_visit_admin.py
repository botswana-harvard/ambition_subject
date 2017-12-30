from django.conf import settings
from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from edc_model_admin import audit_fieldset_tuple, audit_fields
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple, visit_schedule_fields
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import ambition_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectVisit, SubjectRequisition
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectVisit, site=ambition_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = SubjectVisitForm

    requisition_model = SubjectRequisition

    radio_fields = {
        'reason': admin.VERTICAL,
        'reason_unscheduled': admin.VERTICAL,
        'info_source': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_missed',
                'reason_unscheduled',
                'reason_unscheduled_other',
                'info_source',
                'info_source_other',
                'comments']}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple)

    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        'info_source',
        'created',
        'user_created',
    )

    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_code',
    )

    search_fields = (
        'appointment__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj) + audit_fields
                + visit_schedule_fields)

    def view_on_site(self, obj):
        dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
            'subject_dashboard_url')
        try:
            return reverse(
                dashboard_url_name, kwargs=dict(
                    subject_identifier=obj.subject_identifier,
                    appointment=str(obj.appointment.id)))
        except NoReverseMatch:
            return super().view_on_site(obj)
