# Generated by Django 5.2.4 on 2025-07-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('company', models.CharField(max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
