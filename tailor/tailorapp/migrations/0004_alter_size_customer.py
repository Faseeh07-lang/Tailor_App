# Generated by Django 5.1.4 on 2025-03-06 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailorapp', '0003_alter_size_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='customer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='tailorapp.customer'),
        ),
    ]
