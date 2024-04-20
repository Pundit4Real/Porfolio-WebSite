# Generated by Django 5.0 on 2024-04-18 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_hero_favicon_hero_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'ServiceHero',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_no', models.IntegerField(default='0')),
                ('service_title', models.CharField(default='', max_length=150)),
                ('service_desc', models.TextField(default='', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServicePopUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modal_img', models.ImageField(default='', upload_to='popUp modal')),
                ('sub_title', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=700)),
                ('process_descr', models.TextField(default='', max_length=400)),
                ('Process_list', models.CharField(blank=True, max_length=1000)),
                ('service_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.services')),
            ],
            options={
                'verbose_name_plural': 'ServicePopUp',
            },
        ),
    ]