# Generated by Django 2.1.7 on 2019-03-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20190325_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='floor_plan',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]