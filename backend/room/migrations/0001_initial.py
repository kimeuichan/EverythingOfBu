# Generated by Django 2.1.7 on 2019-03-20 08:38

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import room.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('photo', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(null=True, upload_to=room.models.room_photo_path), size=None)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomReview', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('price', models.IntegerField()),
                ('is_lived', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('population', models.SmallIntegerField(default=1)),
                ('deposit', models.IntegerField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='room.Room')),
                ('writter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
