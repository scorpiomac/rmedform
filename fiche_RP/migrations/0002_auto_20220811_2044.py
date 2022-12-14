# Generated by Django 3.1.2 on 2022-08-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiche_RP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='informations',
            new_name='information',
        ),
    ]
