# Generated by Django 2.1.3 on 2018-11-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themet', '0002_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
