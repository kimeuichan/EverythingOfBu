# Generated by Django 2.1.7 on 2019-04-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0002_auto_20190412_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='start_date',
            field=models.DateField(),
        ),
    ]
