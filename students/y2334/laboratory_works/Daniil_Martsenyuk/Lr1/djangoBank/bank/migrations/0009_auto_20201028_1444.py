# Generated by Django 3.0.5 on 2020-10-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20201028_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='refundAmount',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='refund_date',
        ),
    ]
