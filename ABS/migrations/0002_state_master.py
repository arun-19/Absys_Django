# Generated by Django 5.0.6 on 2024-05-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('disc_per', models.CharField(max_length=200)),
            ],
        ),
    ]
