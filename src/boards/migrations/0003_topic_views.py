# Generated by Django 2.1.10 on 2019-09-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190924_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
