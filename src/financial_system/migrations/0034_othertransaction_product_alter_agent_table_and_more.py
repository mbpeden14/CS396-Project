# Generated by Django 4.1.3 on 2022-11-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0033_alter_agent_options_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='othertransaction',
            name='product',
            field=models.CharField(default='', max_length=125),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='agent',
            table='financial_system_agent',
        ),
        migrations.AlterModelTable(
            name='user',
            table='financial_system_user',
        ),
    ]