# Generated by Django 4.1.2 on 2022-10-24 04:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('code_postal', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=100)),
                ('additional_info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('end_date', models.TimeField(blank=True, null=True)),
                ('duration', models.IntegerField(default=1)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events_manager.venue')),
            ],
        ),
    ]