# Generated by Django 3.1.3 on 2020-12-01 01:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201130_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamgroup',
            name='page_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]
