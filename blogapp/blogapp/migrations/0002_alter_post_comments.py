# Generated by Django 5.0.6 on 2024-07-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
