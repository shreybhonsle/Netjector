# Generated by Django 4.0.1 on 2022-01-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
