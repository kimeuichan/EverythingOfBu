# Generated by Django 2.1.7 on 2019-04-13 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0003_auto_20190413_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='topic_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='Vote.Topic'),
        ),
    ]
