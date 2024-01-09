# Generated by Django 4.2.7 on 2023-11-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0008_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='bookrent',
            name='rented_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookrent',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
