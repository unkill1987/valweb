# Generated by Django 2.1.2 on 2018-11-01 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pw', models.CharField(max_length=20)),
                ('c_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
