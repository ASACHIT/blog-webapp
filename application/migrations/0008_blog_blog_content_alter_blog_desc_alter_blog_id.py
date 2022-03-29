# Generated by Django 4.0.3 on 2022-03-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0007_alter_blog_read_more_alter_blog_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_content",
            field=models.TextField(default=" "),
        ),
        migrations.AlterField(
            model_name="blog",
            name="desc",
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name="blog",
            name="id",
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]