# Generated by Django 2.0.1 on 2018-01-14 22:09

from django.db import migrations
from edc_sync.signals import serialize_on_save
from django.db.models.signals import post_save


def update_metadata(apps, schema_editor):
    Panel = apps.get_model('edc_lab.panel')
    RequisitionMetadata = apps.get_model('edc_metadata.requisitionmetadata')
    post_save.disconnect(receiver=serialize_on_save,
                         dispatch_uid='serialize_on_save')
    for obj in RequisitionMetadata.objects.all():
        try:
            panel = Panel.objects.get(display_name=obj.panel_name)
        except Panel.DoesNotExist:
            pass
        else:
            obj.panel_name = panel.name
            obj.save_base(update_fields=['panel_name'])


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0018_auto_20180114_1459'),
    ]

    operations = [migrations.RunPython(update_metadata), ]