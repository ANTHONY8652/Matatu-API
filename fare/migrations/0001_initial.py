# Generated by Django 5.0.7 on 2024-12-03 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_distance', models.FloatField()),
                ('max_distance', models.FloatField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_type', models.CharField(choices=[('M-pesa', 'M-pesa'), ('Cash', 'Cash'), ('Courage', 'Courage'), ('Kidney', 'Kidney')], max_length=10)),
                ('currency', models.CharField(default='KES', max_length=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fares', to='route.route')),
            ],
        ),
    ]