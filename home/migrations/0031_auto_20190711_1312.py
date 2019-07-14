# Generated by Django 2.2.3 on 2019-07-11 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20190711_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='classroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='attendance_classroom', to='home.Classroom'),
        ),
        migrations.AddField(
            model_name='templates',
            name='notes',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='recipient_classrooms',
            field=models.ManyToManyField(related_name='recipient_classroom', to='home.Classroom'),
        ),
    ]
