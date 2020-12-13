# Generated by Django 3.1.2 on 2020-12-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20201130_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_location', models.CharField(max_length=50, verbose_name='Origin Place')),
                ('airport_code', models.CharField(max_length=10, verbose_name='Origin Airport Code')),
                ('airport_lat', models.FloatField()),
                ('airport_lon', models.FloatField()),
            ],
        ),
    ]