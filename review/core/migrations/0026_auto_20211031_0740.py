# Generated by Django 3.1.2 on 2021-10-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201230_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='light_logo_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='logo_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]