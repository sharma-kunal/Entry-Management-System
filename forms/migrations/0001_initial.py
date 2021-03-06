# Generated by Django 2.2.7 on 2019-11-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.TextField()),
                ('visitor_number', models.TextField()),
                ('visitor_email', models.EmailField(max_length=254)),
                ('curr_time', models.TextField()),
                ('host_name', models.TextField()),
                ('host_number', models.TextField()),
                ('host_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
