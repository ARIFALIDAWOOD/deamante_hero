# Generated by Django 2.1.7 on 2019-03-27 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190326_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Specific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prop', models.CharField(max_length=200)),
                ('prop_Id', models.CharField(max_length=20)),
                ('prop_address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('locality', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]