# Generated by Django 5.0.7 on 2024-08-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_useraccount_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='profile_img',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='account_type',
            field=models.CharField(choices=[('savings', 'savings'), ('current', 'current')], max_length=100),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Custom', 'Custom'), ('Male', 'Male')], max_length=100),
        ),
    ]
