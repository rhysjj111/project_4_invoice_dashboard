# Generated by Django 4.2.11 on 2024-03-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_rename_uniqueid_invoice_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]