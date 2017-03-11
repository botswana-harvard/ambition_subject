from edc_constants.constants import OTHER, NOT_APPLICABLE, UNKNOWN

ABNORMAL_RESULTS_REASON = (
    ('cerebral_oedema', 'Cerebral oedema'),
    ('hydrocephalus', 'Hydrocephalus'),
    ('cryptococcomus', 'Cryptococcomus'),
    ('dilated_virchow_robin_spaces', 'Dilated Virchow robin spaces'),
    ('enhancing_mass_lesions', 'Enhancing mass lesions DD Toxoplasmosis, TB, '
                               'lymphoma'),
    ('infarcts', 'Infarcts'),
    (OTHER, 'Other, please specify:'))

ACTION_REQUIRED = (
    ('participant_to_remain', 'Participant to remain on trial'),
    ('participant_to_be_withdrawn', 'participant to be withdrawn from trial'),
    ('patient_remains_on_study', 'Patient remains on study but data analysis '
     'will be modified'))

AE_INTENSITY = (
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'))

AE_SEVERITY = (
    ('grade_3', 'Grade 3- Severe'),
    ('grade_4', 'Grade 4- Life-threatening'),
    ('grade_5', 'Grade 5- Death'))

ANTIBIOTICS = (
    ('amoxicillin', 'Amoxicillin'),
    ('doxycycline', 'Doxycycline'),
    ('flucloxacillin', 'Flucloxacillin'),
    ('ceftriaxone', 'Ceftriaxone'),
    ('erythromycin', 'Erythromycin (contra-indicated with concomitant high  '
                     'dose fluconazole)'),
    ('ciprofloxacin', 'Ciprofloxacin (avoid with concomitant high dose '
                      'fluconazole)'),
    (OTHER, 'Other, specify'))

ARV_REGIMEN = (
    ('TDF +3TC/FTC + either EFZ or NVP', 'TDF +3TC/FTC + either EFZ or NVP'),
    ('AZT + 3-TC + either EFV or NVP', 'AZT + 3-TC + either EFV or NVP'),
    ('d4T + 3-TC + either EFV or NVP', 'd4T + 3-TC + either EFV or NVP'),
    ('TDF + 3TC/FTC + either ATZ/r or Lopinavir/r',
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    ('AZT + 3TC + either ATZ/r or Lopinavir/r',
     'AZT + 3TC + either ATZ/r or Lopinavir/r'))

BRAIN_IMAGINING_REASON = (
    ('reduction_in_gcs', 'Reduction in GCS'),
    ('new_neurology', 'New neurology'),
    (OTHER, 'Other, specify'))

CAUSE_OF_DEATH = (
    ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
    ('Cryptococcal_meningitis_relapse_IRIS', 'Cryptococcal meningitis '
     'relapse/IRIS'),
    ('TB', 'TB'),
    ('bacteraemia', 'Bacteraemia'),
    ('bacterial_pneumonia', 'Bacterial pneumonia'),
    ('malignancy', 'Malignancy'),
    ('art_toxicity', 'ART toxicity'),
    ('IRIS_non_CM', 'IRIS non-CM'),
    ('diarrhea_wasting', 'Diarrhea/wasting'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other, specify'))


CLINICAL_ASSESSMENT = (
    (NOT_APPLICABLE, 'Not applicable'))

CXR_TYPE = (
    ('normal', 'Normal'),
    ('hilar_adenopathy', 'Hilar adenopathy'),
    ('miliary_appearance', 'Miliary appearance'),
    ('pleural_effusion', 'Pleural effusion'),
    ('infiltrate_location', 'Infiltrate-Location'))

DR_OPINION = (
    ('cm_release', 'CM Relapse'),
    ('cm_iris', 'CM IRIS'),
    (OTHER, 'Other, specify'))

FIRST_LINE_REGIMEN = (
    ('EFV', 'EFV'),
    ('NVP', 'NVP'))

FLUCONAZOLE_DOSE = (
    ('400mg_daily', '400mg daily'),
    ('800mg_daily', '800mg daily'),
    (OTHER, 'Other, please specify:'))

INFILTRATE_LOCATION = (
    ('lul', 'LUL'),
    ('lll', 'LLL'),
    ('rul', 'RUL'),
    ('rll', 'RLL')
    ('rml', 'RML'),
    ('diffuse', 'Diffuse'))

MEDICATION_HISTORY = (
    ('TMP-SMX', 'TMP-SMX'),
    (OTHER, 'Other, specify:'))

GLASGOW_COMA_SCORE_EYES = (
    ('does_not_open_eyes', 'Does not open eyes'),
    ('opens_eyes_to_pain_only', 'Opens eyes to pain only'),
    ('opens_eyes_to_voice', 'Opens eyes to voice'),
    ('opens_eyes_spontaneously', 'Opens eyes spontaneously'),
    (NOT_APPLICABLE, 'Not Applicable'))

GLASGOW_COMA_SCORE_VERBAL = (
    ('makes_no_sounds', 'Makes no sounds'),
    ('makes_sounds', 'Makes sounds'),
    ('makes_words', 'Makes words'),
    ('disoriented', 'Disoriented'),
    ('oriented', 'Oriented'),
    (NOT_APPLICABLE, 'Not Applicable'))

GLASGOW_COMA_SCORE_MOTOR = (
    ('makes_no_movement', 'Makes no movement'),
    ('extension_to_pain', 'Extension to pain'),
    ('flexion_to_pain', 'Flexion to pain'),
    ('withdraws_from_pain', 'Withdraws from pain'),
    ('localizes_pain', 'Localizes pain'),
    ('obey_commands', 'Obey commands'))

LP_REASON = (
    ('scheduled_per_protocol', 'Scheduled per protocol'),
    ('therapeutic_lp', 'Therapeutic LP'),
    ('suspected_IRIS_relapse', 'Suspected IRIS relapse'))

MEDICINES = (
    ('fluconazole', 'Fluconazole'),
    ('rifampicin', 'Rifampicin'),
    ('co_trimoxazole', 'Co-trimoxazole'),
    (OTHER, 'Other, specify:'))

PATIENT_TREATMENT_GROUP = (
    ('regimen_1', 'Regimen 1 (Ambisome 10 mg/kg day 1 (single dose))'),
    ('regimen_2', 'Regimen 2 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg day 3 '
                  '(two doses))'),
    ('regimen_3', 'Regimen 3 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg days '
                  '3, and 7 (three doses))'),
    ('regimen_4', 'Regimen 4 (Ambisome 3 mg/kg/d for 14 days (standard dose'
                  ', control arm))'))

PROTOCOL_VIOLATION = (
    ('failure_to_obtain_informed_consent', 'Failure to obtain informed '
     'consent'),
    ('enrollment_of_ineligible_patient', 'Enrollment of ineligible patient'),
    ('screening_procedure not done', 'Screening procedure required by '
     'protocol not done'),
    ('screening_or_on-study_procedure', 'Screening or on-study procedure/lab '
     'work required not done'),
    ('incorrect_research_treatment', 'Incorrect research treatment given to '
     'patient'),
    ('procedure_not_completed', 'On-study procedure required by protocol not '
     'completed'),
    ('visit_non-compliance', 'Visit non-compliance'),
    ('medication_stopped_early', 'Medication stopped early'),
    ('medication_noncompliance', 'Medication_noncompliance'),
    ('national_regulations_not_met', 'Standard WPD, ICH-GCP, local/national '
     'regulations not met'),
    (OTHER, 'Other'))

RAE_REASON = (
    ('death', 'Death (Please complete Death form and Study termination form)'),
    ('life_threatening', 'Life-threatening'),
    ('significant_disability', 'Significant disability'),
    ('in-patient_hospitalization or prolongation',
     'In-patient hospitalization or prolongation '
     '(beyond 2 weeks from study inclusion)'),
    ('Medically_important_event',
     'Medically important event (e.g. Severe thrombophlebitis, Bacteraemia, '
     'recurrence of symptoms not requiring admission, Hospital acquired '
     'pneumonia)'))

REASON_DRUG_MISSED = (
    ('administered_to_protocol', 'Administered acc to protocol'),
    ('toxicity', 'Toxicity'),
    ('missed', 'Missed'),
    ('refused', 'Refused'),
    (OTHER, 'Other'),
    ('not_required_acc_protocol', 'Not required according to protocol'))

STEROIDS_CHOICES = (
    ('oral_prednisolone', 'Oral prednisolone'),
    ('iv_dexamethasone', 'IV Dexamethasone used'),
    (OTHER, 'Other, specify:'))

STUDY_DRUG_RELATIONSHIP = (
    ('not_related', 'Not related'),
    ('unlikely_related', 'Unlikely related'),
    ('possibly_related', 'Possibly related'),
    ('probably_related', 'Probably related'),
    ('definitely_related', 'Definitely related'),
    (NOT_APPLICABLE, 'Not Applicable'))

REASON_DRUG_MISSED = (
    ('A', 'Administered acc to protocol'),
    ('T', 'Toxicity'),
    ('M', 'Missed'),
    ('R', 'Refused'),
    (OTHER, 'Other'),
    ('N', 'Not required according to protocol'))

TB_SITE = (
    ('pulmonary', 'Pulmonary'),
    ('extra_pulmonary', 'Extra pulmonary'))

TB_SITE_DEATH = (
    ('meningitis', 'Meningitis'),
    ('pulmonary', 'Pulmonary'),
    ('disseminated', 'Disseminated'))

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology',
     'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'))
