# Generated by Django 2.2 on 2019-05-29 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_systemadmin'),
        ('books', '0006_auto_20190529_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreBooks_of_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Bookstore_books')),
                ('newuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.User')),
            ],
        ),
    ]
