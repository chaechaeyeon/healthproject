# Generated by Django 4.2.2 on 2023-06-21 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lowerbody', '0007_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='writer',
            new_name='author',
        ),
    ]
