# Generated by Django 4.2.1 on 2023-07-07 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_leaderboard_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderboard',
            old_name='members',
            new_name='membersname',
        ),
    ]
