# Generated by Django 2.2 on 2019-05-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0005_auto_20190530_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='categories',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='names_of_books',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_type',
            field=models.IntegerField(null=True),
        ),
    ]
