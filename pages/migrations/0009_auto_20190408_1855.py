# Generated by Django 2.1.7 on 2019-04-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190408_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='display_img',
            field=models.ImageField(height_field='960', null=True, upload_to='photos/%Y/%m/%d/', width_field='1920'),
        ),
    ]
