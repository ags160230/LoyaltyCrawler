# Generated by Django 2.1.7 on 2019-04-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_searchcriteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchcriteria',
            name='in_use',
            field=models.BooleanField(default=False),
        ),
    ]
