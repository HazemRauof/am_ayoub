# Generated by Django 2.2 on 2019-05-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_systemadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]