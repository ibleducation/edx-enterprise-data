# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseEnrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enterprise_id', models.CharField(max_length=255)),
                ('enterprise_name', models.CharField(max_length=255)),
                ('lms_user_id', models.CharField(max_length=255)),
                ('enterprise_user_id', models.CharField(max_length=255)),
                ('course_id', models.CharField(help_text=b'The course the learner is enrolled in.', max_length=255)),
                ('enrollment_created_timestamp', models.DateTimeField()),
                ('user_current_enrollment_mode', models.CharField(max_length=64)),
                ('consent_granted', models.BooleanField()),
                ('letter_grade', models.CharField(max_length=1)),
                ('has_passed', models.BooleanField()),
                ('passed_timestamp', models.DateTimeField()),
                ('enterprise_sso_user_id', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_start', models.DateTimeField()),
                ('course_end', models.DateTimeField()),
                ('course_pacing_type', models.CharField(max_length=255)),
                ('course_duration_weeks', models.PositiveIntegerField()),
                ('course_min_effort', models.CharField(max_length=100)),
                ('course_max_effort', models.CharField(max_length=100)),
                ('user_account_creation_date', models.DateTimeField()),
                ('user_email', models.CharField(max_length=255)),
                ('user_username', models.CharField(max_length=255)),
                ('user_age', models.PositiveIntegerField()),
                ('user_level_of_education', models.CharField(max_length=6)),
                ('user_gender', models.CharField(max_length=6)),
                ('user_country_code', models.CharField(max_length=3)),
                ('country_name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Enterprise Enrollment',
                'verbose_name_plural': 'Enterprise Enrollments',
            },
        ),
    ]
