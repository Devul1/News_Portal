# Generated by Django 4.1.3 on 2023-02-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_type',
            field=models.CharField(choices=[('NW', 'News'), ('AR', 'Article')], default='NW', max_length=2),
        ),
    ]
