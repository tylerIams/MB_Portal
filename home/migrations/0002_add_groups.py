from django.db import models, migrations
from home.models.models import Group
from django.conf import settings


def add_groups(apps, schema_editor):
    """This migration guarantees that group IDs are generated correctly.  See missionbit/settings.py
    for group ID settings"""
    Group.objects.get_or_create(name="student")
    Group.objects.get_or_create(name="staff")
    Group.objects.get_or_create(name="donor")
    Group.objects.get_or_create(name="teacher")
    Group.objects.get_or_create(name="volunteer")


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0011_update_proxy_permissions"),
        ("home", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_groups)]
