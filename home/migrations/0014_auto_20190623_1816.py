# Generated by Django 2.2.1 on 2019-06-23 18:16

from django.db import migrations
import django.db.models.deletion
import salesforce.backend.operations
import salesforce.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190622_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='npe01_systemis_individual',
            field=salesforce.fields.BooleanField(db_column='npe01__SYSTEMIsIndividual__c', default=salesforce.backend.operations.DefaultedOnCreate(), help_text='Indicates whether or not this Account is special for Contacts (Household, One-to-One, Individual) vs a normal Account.', verbose_name='_SYSTEM: IsIndividual'),
        ),
        migrations.AddField(
            model_name='contact',
            name='account',
            field=salesforce.fields.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_account_set', to='home.Account'),
        ),
        migrations.AddField(
            model_name='contact',
            name='current_grade_level',
            field=salesforce.fields.CharField(blank=True, db_column='Current_grade_level__c', max_length=1300, null=True, verbose_name='Current grade level'),
        ),
        migrations.AddField(
            model_name='contact',
            name='dm_current_grade',
            field=salesforce.fields.CharField(blank=True, choices=[('Graduating 8th', 'Graduating 8th'), ('Freshman, 9th', 'Freshman, 9th'), ('Sophomore, 10th', 'Sophomore, 10th'), ('Junior, 11th', 'Junior, 11th'), ('Senior, 12th', 'Senior, 12th')], db_column='DM_Current_grade__c', help_text='Need this for data migration to calculate Expected Graduation Year?  If not, delete this field.', max_length=255, null=True, verbose_name='DM - Current grade'),
        ),
        migrations.AddField(
            model_name='contact',
            name='enrollments_this_semester_applied',
            field=salesforce.fields.DecimalField(blank=True, db_column='enrollments_this_semester_Applied__c', decimal_places=0, help_text='DO NOT EDIT - AUTO-POPULATED BY SYSTEM', max_digits=2, null=True, verbose_name='# enrollments this semester - Applied'),
        ),
        migrations.AddField(
            model_name='contact',
            name='enrollments_this_semester_drop_out',
            field=salesforce.fields.DecimalField(blank=True, db_column='enrollments_this_semester_Drop_out__c', decimal_places=0, help_text='DO NOT EDIT - AUTO-POPULATED BY SYSTEM', max_digits=2, null=True, verbose_name='# enrollments this semester - Drop out'),
        ),
        migrations.AddField(
            model_name='contact',
            name='enrollments_this_semester_rejected',
            field=salesforce.fields.DecimalField(blank=True, db_column='enrollments_this_semester_Rejected__c', decimal_places=0, help_text='DO NOT EDIT - AUTO-POPULATED BY SYSTEM', max_digits=2, null=True, verbose_name='# enrollments this semester - Rejected'),
        ),
        migrations.AddField(
            model_name='contact',
            name='enrollments_this_semester_waitlisted',
            field=salesforce.fields.DecimalField(blank=True, db_column='enrollments_this_semester_Waitlisted__c', decimal_places=0, help_text='DO NOT EDIT - AUTO-POPULATED BY SYSTEM', max_digits=2, null=True, verbose_name='# enrollments this semester - Waitlisted'),
        ),
        migrations.AddField(
            model_name='contact',
            name='expected_graduation_year',
            field=salesforce.fields.CharField(blank=True, db_column='Expected_graduation_year__c', help_text='Enter the year this contact is expected to graduate.  For example, 2020', max_length=4, null=True, verbose_name='Expected graduation year'),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=salesforce.fields.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Genderqueer/Gender Non-binary', 'Genderqueer/Gender Non-binary'), ('Trans Female', 'Trans Female'), ('Trans Male', 'Trans Male'), ('Other', 'Not Listed')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender_other',
            field=salesforce.fields.CharField(blank=True, db_column='Gender_Other__c', max_length=50, null=True, verbose_name='Gender (Other)'),
        ),
        migrations.AddField(
            model_name='contact',
            name='parent_guardian_email',
            field=salesforce.fields.EmailField(blank=True, db_column='Parent_Guardian_email__c', max_length=254, null=True, verbose_name='Parent/Guardian email'),
        ),
        migrations.AddField(
            model_name='contact',
            name='parent_guardian_first_name',
            field=salesforce.fields.CharField(blank=True, db_column='Parent_Guardian_first_name__c', max_length=100, null=True, verbose_name='Parent/Guardian first name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='parent_guardian_last_name',
            field=salesforce.fields.CharField(blank=True, db_column='Parent_Guardian_last_name__c', max_length=100, null=True, verbose_name='Parent/Guardian last name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='parent_guardian_phone',
            field=salesforce.fields.CharField(blank=True, db_column='Parent_Guardian_phone__c', max_length=40, null=True, verbose_name='Parent/Guardian phone'),
        ),
        migrations.AddField(
            model_name='contact',
            name='race',
            field=salesforce.fields.CharField(blank=True, choices=[('American Indian/Alaskan Native', 'American Indian/Alaskan Native'), ('Asian', 'Asian'), ('Black/African American', 'Black/African American'), ('Native Hawaiian/Other Pacific Islander', 'Native Hawaiian/Other Pacific Islander'), ('White', 'White'), ('American Indian/Alaskan Native AND Black/African American', 'American Indian/Alaskan Native AND Black/African American'), ('American Indian/Alaskan Native AND White', 'American Indian/Alaskan Native AND White'), ('Asian AND White', 'Asian AND White'), ('Black/African American AND White', 'Black/African American AND White'), ('Other/Multiracial', 'Other/Multiracial')], max_length=255, null=True, verbose_name='Which best describes your race?'),
        ),
        migrations.AddField(
            model_name='contact',
            name='race_other',
            field=salesforce.fields.CharField(blank=True, db_column='Race_Other__c', max_length=100, null=True, verbose_name='Which best describes your race? (Other)'),
        ),
        migrations.AddField(
            model_name='contact',
            name='volunteer_area_s_of_interest',
            field=salesforce.fields.CharField(blank=True, choices=[('Classroom', 'Classroom'), ('Event', 'Event'), ('Other', 'Other')], db_column='Volunteer_area_s_of_interest__c', max_length=4099, null=True, verbose_name='Volunteer area(s) of interest'),
        ),
        migrations.AddField(
            model_name='contact',
            name='which_best_describes_your_ethnicity',
            field=salesforce.fields.CharField(blank=True, choices=[('Hispanic/Latinx', 'Hispanic/Latinx'), ('Not Hispanic/Latinx', 'Not Hispanic/Latinx')], db_column='Which_best_describes_your_ethnicity__c', max_length=255, null=True, verbose_name='Which best describes your ethnicity?'),
        ),
    ]
