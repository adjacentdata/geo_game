# Generated by Django 4.0 on 2021-12-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='user_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='user_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]