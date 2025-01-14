# Generated by Django 5.0.6 on 2024-10-06 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0006_remove_blog_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='userpanel_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
