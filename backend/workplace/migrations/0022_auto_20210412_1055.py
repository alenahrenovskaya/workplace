# Generated by Django 3.0.3 on 2021-04-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0021_auto_20210412_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='ended',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='started',
            field=models.DateField(null=True),
        ),
    ]
