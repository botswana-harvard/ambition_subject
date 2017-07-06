from django import forms

from ambition_subject_validations.form_validators import Week2FormValidator

from ..models import (
    Week2, AmphotericinMissedDoses, FluconazoleMissedDoses, SignificantDiagnoses)
from .form_mixins import SubjectModelFormMixin


class Week2Form(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Week2FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Week2
        fields = '__all__'


class SignificantDiagnosesForm(forms.ModelForm):

    class Meta:
        model = SignificantDiagnoses
        fields = '__all__'


class FluconazoleMissedDosesForm(forms.ModelForm):

    class Meta:
        model = FluconazoleMissedDoses
        fields = '__all__'


class AmphotericinMissedDosesForm(forms.ModelForm):

    class Meta:
        model = AmphotericinMissedDoses
        fields = '__all__'
