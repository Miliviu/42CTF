# Generated by Django 3.1.3 on 2021-06-08 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofileinfo_discord_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'ordering': ['-score', 'last_submission_date', 'user__username'], 'permissions': (('view_info', 'View user info'),), 'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
    ]
