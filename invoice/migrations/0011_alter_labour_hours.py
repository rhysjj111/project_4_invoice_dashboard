# Generated by Django 4.2.11 on 2024-04-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_remove_labour_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
