# Generated by Django 3.1.3 on 2021-01-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='modified',
            field=models.DateTimeField(editable=False),
        ),
    ]