# Generated by Django 4.1.3 on 2022-11-06 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0022_transactiontypes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactiontypes',
            options={'verbose_name': 'Transaction Type'},
        ),
    ]