# Generated by Django 3.2.6 on 2021-08-31 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_remove_about_career'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
