# Generated by Django 4.0.3 on 2022-03-20 16:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0010_alter_blog_blog_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
