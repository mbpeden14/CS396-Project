# Generated by Django 4.1.3 on 2022-11-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0052_liststocksondate_stock_date_alter_agent_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liststocksondate',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='listusertransactions',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='othertransaction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='propertytransaction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
