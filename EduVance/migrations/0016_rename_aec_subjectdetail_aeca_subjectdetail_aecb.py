# Generated by Django 5.1.4 on 2025-04-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0015_subjectdetail_elective_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectdetail',
            old_name='aec',
            new_name='aeca',
        ),
        migrations.AddField(
            model_name='subjectdetail',
            name='aecb',
            field=models.TextField(blank=True, null=True),
        ),
    ]
