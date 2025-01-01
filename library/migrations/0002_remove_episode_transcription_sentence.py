# Generated by Django 5.1.4 on 2025-01-01 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='transcription',
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('start_time', models.FloatField()),
                ('end_time', models.FloatField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='library.episode')),
            ],
        ),
    ]
