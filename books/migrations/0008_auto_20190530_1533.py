# Generated by Django 2.2 on 2019-05-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_storebooks_of_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='Book_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
