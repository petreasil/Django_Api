# Generated by Django 3.2.7 on 2021-09-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('completed', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
