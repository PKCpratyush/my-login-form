# Generated by Django 4.0 on 2021-12-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='our_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(max_length=50)),
                ('user_id', models.TextField(max_length=50)),
                ('user_password', models.TextField(max_length=8)),
            ],
        ),
    ]
