# Generated by Django 4.1.2 on 2023-01-26 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_alter_room_amenities_alter_room_category_and_more"),
        ("medias", "0002_alter_photo_file_alter_video_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
    ]