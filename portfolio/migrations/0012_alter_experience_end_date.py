# Generated by Django 3.2.6 on 2021-08-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_experience_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
