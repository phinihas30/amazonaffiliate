# Generated by Django 5.0.2 on 2025-07-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliateproduct',
            name='temp',
            field=models.CharField(default='', max_length=1),
        ),
    ]
