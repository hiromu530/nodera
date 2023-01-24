# Generated by Django 4.1.2 on 2022-12-21 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='作成時刻', verbose_name='作成時刻')),
                ('topictitle', models.CharField(default='トピックタイトル', max_length=20, verbose_name='トピックタイトル')),
                ('itemid', models.CharField(default='0', max_length=10, verbose_name='id')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='トピックタイトル')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='更新日時', verbose_name='更新日時')),
            ],
            options={
                'db_table': 'topics',
            },
        ),
    ]
