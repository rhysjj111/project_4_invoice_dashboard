# Generated by Django 4.2.11 on 2024-03-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_rename_post_code_customer_postcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
