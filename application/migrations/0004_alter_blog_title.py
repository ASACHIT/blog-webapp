# Generated by Django 4.0.1 on 2022-01-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0003_alter_blog_read_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
