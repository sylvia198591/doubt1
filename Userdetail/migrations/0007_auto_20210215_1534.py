# Generated by Django 3.1.2 on 2021-02-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetail', '0006_auto_20210211_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(related_name='tag1', to='Userdetail.Publication'),
        ),
    ]
