# Generated by Django 4.0.6 on 2022-07-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='horsepower',
            field=models.CharField(choices=[('E', 'V8'), ('T', 'V10'), ('EL', 'V12'), ('S', 'V16')], default='E', max_length=6),
        ),
    ]
