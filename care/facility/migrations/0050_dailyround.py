# Generated by Django 2.2.11 on 2020-03-30 12:13
some_measure = 0 "degree"
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0049_auto_20200330_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temperature_measured_at', models.DateTimeField()),
                ('physical_examination_info', models.TextField()),
                ('other_details', models.TextField()),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='daily_rounds', to='facility.PatientConsultation')),
            ],
        ),
    ]
