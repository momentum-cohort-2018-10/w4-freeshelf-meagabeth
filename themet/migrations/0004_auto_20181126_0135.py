# Generated by Django 2.1.3 on 2018-11-26 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themet', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='book',
            name='african_art',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='american_art',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='european_art',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='medival_art',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='twentieth_cent_art',
            field=models.BooleanField(default=False),
        ),
    ]