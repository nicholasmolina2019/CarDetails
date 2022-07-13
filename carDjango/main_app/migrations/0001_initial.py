# Generated by Django 4.0.6 on 2022-07-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]