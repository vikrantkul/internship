# Generated by Django 3.1.7 on 2021-03-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacityrevenue', '0003_capacity_revenue_table_no_of_years'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacity_revenue_table',
            old_name='date',
            new_name='output_date',
        ),
    ]
