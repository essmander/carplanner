# Generated by Django 3.0.6 on 2020-06-06 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('customer', models.CharField(max_length=50)),
                ('project_number', models.CharField(max_length=50)),
                ('user_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_made', to=settings.AUTH_USER_MODEL, verbose_name='Who is making the reservation')),
            ],
        ),
    ]
