# Generated by Django 2.2.3 on 2019-07-31 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_add_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dismissed', models.BooleanField(default=False)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_distributed', to='home.Announcement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
