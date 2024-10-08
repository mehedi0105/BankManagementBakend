# Generated by Django 5.0.7 on 2024-08-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_type',
            field=models.CharField(choices=[('savings', 'savings'), ('current', 'current')], max_length=100),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('Custom', 'Custom'), ('Male', 'Male'), ('Female', 'Female')], max_length=100),
        ),
    ]
