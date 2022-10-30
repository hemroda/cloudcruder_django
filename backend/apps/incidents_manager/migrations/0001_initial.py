# Generated by Django 4.1.2 on 2022-10-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]