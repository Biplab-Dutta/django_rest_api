# Generated by Django 3.1.7 on 2021-04-02 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='isStaff',
            new_name='is_staff',
        ),
    ]
