# Generated by Django 4.1.2 on 2022-12-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="perks",
            field=models.ManyToManyField(to="experiences.perk"),
        ),
        migrations.AddField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, default="", max_length=250),
        ),
        migrations.AddField(
            model_name="perk",
            name="explanation",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="perk",
            name="name",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
