# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-04-25 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('sms_number', models.BigIntegerField(null=True)),
                ('whatsapp_number', models.BigIntegerField(null=True)),
                ('area', models.CharField(max_length=200)),
                ('location', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Moderator')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
            },
        ),
        migrations.CreateModel(
            name='City_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('city_code', models.CharField(max_length=10)),
                ('whatsapp', models.BooleanField(default=True)),
                ('sms', models.BooleanField(default=True)),
                ('distress', models.BooleanField(default=False)),
                ('distress_contact', models.CharField(blank=True, max_length=13, null=True)),
                ('taxi_no', models.BigIntegerField(default=0)),
                ('police_no', models.BigIntegerField(default=0)),
                ('complaint_no', models.BigIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'City Code',
                'verbose_name_plural': 'City Codes',
            },
        ),
        migrations.CreateModel(
            name='Complaint_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_number', models.CharField(max_length=20)),
                ('area', models.CharField(default='', max_length=200)),
                ('origin_area', models.CharField(blank=True, max_length=200, null=True)),
                ('destination_area', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('complaint', models.CharField(blank=True, max_length=100, null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxiapp.City_Code')),
            ],
            options={
                'verbose_name': 'Customer Complaint',
                'verbose_name_plural': 'Customer Complaints',
            },
        ),
        migrations.CreateModel(
            name='Otp_Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OTP Code',
                'verbose_name_plural': 'OTP Codes',
            },
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Complaint Reason',
                'verbose_name_plural': 'Complaint Reasons',
            },
        ),
        migrations.CreateModel(
            name='Taxi_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=24)),
                ('traffic_number', models.CharField(default='', max_length=28, unique=True)),
                ('driver_name', models.CharField(max_length=40, verbose_name='Name')),
                ('son_of', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('aadhar_number', models.CharField(blank=True, max_length=22, null=True)),
                ('driving_license_number', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_validity', models.DateField(blank=True, null=True)),
                ('autostand', models.CharField(blank=True, max_length=80, null=True, verbose_name='Stand')),
                ('union', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance', models.DateField(blank=True, null=True)),
                ('capacity_of_passengers', models.CharField(blank=True, max_length=14, null=True)),
                ('pollution', models.DateField(blank=True, null=True)),
                ('engine_number', models.CharField(blank=True, max_length=40, null=True)),
                ('chasis_number', models.CharField(blank=True, max_length=30, null=True)),
                ('owner_driver', models.CharField(blank=True, choices=[('OWNER', 'Owner'), ('DRIVER', 'Driver')], default='OWNER', max_length=6, null=True)),
                ('num_of_complaints', models.BigIntegerField(default=0)),
                ('driver_image', models.ImageField(default='drivers/profile.png', upload_to='drivers')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr')),
                ('driver_image_name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxidetails', to='taxiapp.City_Code')),
            ],
            options={
                'verbose_name': 'Driver/Owner',
                'verbose_name_plural': 'Drivers & Owners',
            },
        ),
        migrations.AddField(
            model_name='complaint_statement',
            name='reason',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taxiapp.Reasons'),
        ),
        migrations.AddField(
            model_name='complaint_statement',
            name='taxi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxiapp.Taxi_Detail', verbose_name='Vehicle ID'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taxiapp.City_Code'),
        ),
    ]