# Generated by Django 4.2.1 on 2023-05-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicksapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
    ]
