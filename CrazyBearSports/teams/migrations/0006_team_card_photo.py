# Generated by Django 3.1.3 on 2020-12-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_teamgroup_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='card_photo',
            field=models.ImageField(null=True, upload_to='team_card_photos'),
        ),
    ]
