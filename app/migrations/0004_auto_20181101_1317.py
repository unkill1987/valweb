# Generated by Django 2.1.2 on 2018-11-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_member_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_role',
            field=models.CharField(max_length=20),
        ),
    ]
