# Generated by Django 4.0.3 on 2022-03-20 12:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0008_blog_blog_content_alter_blog_desc_alter_blog_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
