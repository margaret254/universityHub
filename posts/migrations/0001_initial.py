# Generated by Django 2.2 on 2020-07-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('home_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
