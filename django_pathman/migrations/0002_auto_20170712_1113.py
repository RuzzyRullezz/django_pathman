# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-12 08:13
from __future__ import unicode_literals

from django.db import migrations

from django_pathman.helpers import read_sql

FORWARDS_SQL = read_sql('alter_child_index_v2.sql')
REVERSE_SQL = read_sql('alter_child_index_v1.sql')


class Migration(migrations.Migration):

    dependencies = [
        ('django_pathman', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(sql=FORWARDS_SQL, reverse_sql=REVERSE_SQL)
    ]