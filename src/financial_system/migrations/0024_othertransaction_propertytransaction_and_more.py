# Generated by Django 4.1.3 on 2022-11-07 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0023_alter_transactiontypes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.IntegerField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Other Product Transaction',
            },
        ),
        migrations.CreateModel(
            name='PropertyTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Property Transaction',
            },
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shares', models.IntegerField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Stock Transaction',
            },
        ),
        migrations.DeleteModel(
            name='UserTransaction',
        ),
    ]
