# Generated by Django 4.2 on 2025-01-12 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_data',
            new_name='updated_date',
        ),
    ]