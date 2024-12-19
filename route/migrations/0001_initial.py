# Generated by Django 5.0.7 on 2024-12-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('end_location', models.CharField(max_length=100)),
                ('distance', models.FloatField()),
                ('estimated_time', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
