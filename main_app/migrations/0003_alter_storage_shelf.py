# Generated by Django 4.1.5 on 2023-01-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='shelf',
            field=models.IntegerField(default=1),
        ),
    ]
