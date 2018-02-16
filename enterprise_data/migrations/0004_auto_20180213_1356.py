# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0003_auto_20180209_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='consent_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_duration_weeks',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_max_effort',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_min_effort',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_pacing_type',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='course_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='enterprise_id',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='enterprise_sso_user_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='enterprise_user_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='has_passed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='letter_grade',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='lms_user_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='passed_timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_account_creation_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_current_enrollment_mode',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_gender',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_level_of_education',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='enterpriseenrollment',
            name='user_username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
