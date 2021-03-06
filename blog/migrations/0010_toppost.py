# Generated by Django 4.0.1 on 2022-02-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='topPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
