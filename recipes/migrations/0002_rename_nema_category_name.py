# Generated by Django 4.1.6 on 2023-02-23 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nema',
            new_name='name',
        ),
    ]