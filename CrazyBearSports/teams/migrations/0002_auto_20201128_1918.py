# Generated by Django 3.1.3 on 2020-11-29 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='TeamGroup',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.teamgroup')),
            ],
        ),
    ]
