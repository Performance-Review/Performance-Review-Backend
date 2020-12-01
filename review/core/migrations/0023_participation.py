# Generated by Django 3.1.2 on 2020-10-31 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_auto_20201006_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_started_self_review', models.BooleanField(default=False)),
                ('has_started_peer_review', models.BooleanField(default=False)),
                ('has_started_manager_review', models.BooleanField(default=False)),
                ('has_started_results', models.BooleanField(default=False)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.round')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]