# Generated by Django 2.1.7 on 2019-03-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20190320_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='First_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='Last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]