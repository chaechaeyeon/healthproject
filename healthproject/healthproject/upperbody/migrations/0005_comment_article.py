# Generated by Django 4.2.1 on 2023-05-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upperbody', '0004_remove_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='upperbody.post'),
        ),
    ]