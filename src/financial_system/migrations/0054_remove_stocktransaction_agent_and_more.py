# Generated by Django 4.1.3 on 2022-11-08 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0053_alter_liststocksondate_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktransaction',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='StockTransaction',
        ),
    ]
