# Generated by Django 2.1.7 on 2019-03-07 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborations', '0007_auto_20190307_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needmember',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='collaborations.Post'),
        ),
    ]
