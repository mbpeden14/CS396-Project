# Generated by Django 4.1.3 on 2022-11-06 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0007_alter_agent_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='agent',
            table='financial_system_agent',
        ),
        migrations.AlterModelTable(
            name='user',
            table='financial_system_user',
        ),
    ]
