# Generated by Django 5.0.6 on 2024-10-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
