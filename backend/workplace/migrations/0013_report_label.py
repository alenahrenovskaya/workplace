# Generated by Django 3.0.3 on 2021-04-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0012_auto_20210404_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='label',
            field=models.TextField(blank=True, null=True),
        ),
    ]
