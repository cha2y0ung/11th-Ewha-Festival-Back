# Generated by Django 3.0.8 on 2022-09-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220906_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_booth',
            field=models.BooleanField(default=True),
        ),
    ]