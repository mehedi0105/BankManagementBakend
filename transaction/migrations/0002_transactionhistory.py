# Generated by Django 5.0.7 on 2024-08-24 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_useraccount_account_type_and_more'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_type', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('paid_in', models.DecimalField(decimal_places=2, max_digits=12)),
                ('paid_out', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount')),
            ],
        ),
    ]
