# Generated by Django 5.0.7 on 2024-08-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_useraccount_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('Custom', 'Custom'), ('Female', 'Female'), ('Male', 'Male')], max_length=100),
        ),
    ]
