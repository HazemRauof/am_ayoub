# Generated by Django 2.2 on 2019-05-29 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0002_reader'),
        ('bookstore', '0002_auto_20190529_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
                ('bstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.User')),
            ],
        ),
    ]