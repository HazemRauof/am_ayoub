# Generated by Django 2.2 on 2019-05-29 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_categories', models.CharField(max_length=100)),
                ('preferred_writers', models.CharField(max_length=100)),
                ('Adress', models.CharField(max_length=100)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.User')),
            ],
        ),
    ]
