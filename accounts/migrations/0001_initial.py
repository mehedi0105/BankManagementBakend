# Generated by Django 5.0.7 on 2024-08-22 15:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='')),
                ('account_type', models.CharField(choices=[('current', 'current'), ('savings', 'savings')], max_length=100)),
                ('account_no', models.IntegerField(unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Custom', 'Custom'), ('Female', 'Female'), ('Male', 'Male')], max_length=100)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField()),
                ('street_address', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
