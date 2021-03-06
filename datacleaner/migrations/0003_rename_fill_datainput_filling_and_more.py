# Generated by Django 4.0.3 on 2022-04-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacleaner', '0002_datainput_fill_alter_datainput_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datainput',
            old_name='fill',
            new_name='filling',
        ),
        migrations.RemoveField(
            model_name='datainput',
            name='fill_null',
        ),
        migrations.AlterField(
            model_name='datainput',
            name='clean_null',
            field=models.BooleanField(choices=[(0, 'Delete'), (1, 'Fill')], default=0, max_length=2),
        ),
    ]
