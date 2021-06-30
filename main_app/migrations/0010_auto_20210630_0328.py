# Generated by Django 3.1.7 on 2021-06-30 03:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.pet'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_to',
            field=models.DateField(default=datetime.date(2021, 7, 1)),
        ),
    ]
