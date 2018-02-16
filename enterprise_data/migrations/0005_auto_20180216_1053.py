# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0004_auto_20180213_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='user_gender',
        ),
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='user_level_of_education',
        ),
    ]
