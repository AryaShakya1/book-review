# Generated by Django 5.0.6 on 2024-06-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]