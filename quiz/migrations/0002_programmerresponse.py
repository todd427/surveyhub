# Generated by Django 5.2.3 on 2025-06-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammerResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('age', models.PositiveIntegerField()),
                ('years', models.PositiveIntegerField()),
                ('primary_language', models.CharField(max_length=64)),
                ('languages', models.CharField(max_length=256)),
                ('other_language', models.CharField(blank=True, max_length=64)),
                ('algorithms', models.CharField(max_length=64)),
                ('data_structures', models.CharField(max_length=64)),
                ('challenges', models.CharField(max_length=256)),
                ('git', models.CharField(max_length=64)),
                ('ci_cd', models.CharField(max_length=64)),
                ('testing', models.CharField(max_length=64)),
                ('open_source', models.CharField(max_length=64)),
                ('largest_project', models.CharField(max_length=128)),
                ('agile', models.CharField(max_length=64)),
                ('architecture', models.CharField(max_length=64)),
                ('concepts', models.CharField(max_length=128)),
                ('deployment', models.CharField(max_length=128)),
                ('platforms', models.CharField(max_length=128)),
                ('platform_other', models.CharField(blank=True, max_length=64)),
                ('interests', models.CharField(max_length=128)),
                ('interests_other', models.CharField(blank=True, max_length=128)),
                ('learning', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
