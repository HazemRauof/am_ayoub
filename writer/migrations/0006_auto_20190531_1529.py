# Generated by Django 2.2 on 2019-05-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0005_auto_20190531_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]