# Generated by Django 3.2.6 on 2021-10-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beepjeep',
            name='beepStatus',
            field=models.IntegerField(),
        ),
    ]
