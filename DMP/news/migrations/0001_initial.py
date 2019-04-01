# Generated by Django 2.1.7 on 2019-03-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(max_length=50)),
                ('Headlines', models.CharField(max_length=200)),
                ('img_disp', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('img_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('summary', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
