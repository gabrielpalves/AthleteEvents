# Generated by Django 4.0.5 on 2022-06-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ek',
            new_name='event_key',
        ),
        migrations.AlterField(
            model_name='event',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='sex',
            field=models.CharField(max_length=1),
        ),
    ]
