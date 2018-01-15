# Generated by Django 2.0.1 on 2018-01-14 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_lab', '0012_auto_20180114_1438'),
        ('ambition_subject', '0015_auto_20180113_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubjectrequisition',
            name='panel',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_lab.Panel'),
        ),
        migrations.AddField(
            model_name='subjectrequisition',
            name='panel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_lab.Panel'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectrequisition',
            name='panel_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subjectrequisition',
            name='panel_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]