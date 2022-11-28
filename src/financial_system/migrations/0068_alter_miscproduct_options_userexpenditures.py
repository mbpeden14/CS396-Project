# Generated by Django 4.1.3 on 2022-11-27 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0067_alter_bond_issuer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscproduct',
            options={'verbose_name': 'Other Product'},
        ),
        migrations.CreateModel(
            name='UserExpenditures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('food', models.DecimalField(decimal_places=2, max_digits=7)),
                ('health', models.DecimalField(decimal_places=2, max_digits=7)),
                ('entertainment', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vehicle_fuel', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('children', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('travel', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('other', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
        ),
    ]