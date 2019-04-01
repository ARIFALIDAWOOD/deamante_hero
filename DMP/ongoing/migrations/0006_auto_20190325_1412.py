# Generated by Django 2.1.7 on 2019-03-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ongoing', '0005_auto_20190322_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoing',
            name='amen1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='amen2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='amen3',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='floor_plan',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='img_disp',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='map_link',
            field=models.CharField(blank=True, max_length=350),
        ),
        migrations.AddField(
            model_name='ongoing',
            name='video_link',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
