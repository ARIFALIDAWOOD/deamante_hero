# Generated by Django 2.1.7 on 2019-03-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ongoing', '0002_auto_20190317_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ongoing',
            name='Bath',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ongoing',
            name='Bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ongoing',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ongoing',
            name='prop_type',
            field=models.CharField(max_length=20),
        ),
    ]
