# Generated by Django 3.2.8 on 2021-10-26 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_tessiu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tessiu',
            name='inflamation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
