# Generated by Django 4.2.3 on 2023-07-18 15:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fantasy_football", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FFDBSeason",
            new_name="FantasyFootballSeason",
        ),
    ]