# Generated by Django 3.0.7 on 2020-06-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendance_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='attendance_signup',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('amount', models.IntegerField(default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendants', to='schedules.Event')),
            ],
            options={
                'ordering': ('event', 'full_name'),
            },
        ),
    ]
