# Generated by Django 4.1.6 on 2023-12-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interact_uz', '0007_authors'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Authors',
        ),
        migrations.RemoveField(
            model_name='free_codes',
            name='type_catg',
        ),
        migrations.RemoveField(
            model_name='telegram_bot',
            name='type_catg',
        ),
        migrations.RemoveField(
            model_name='web_sites',
            name='type_catg',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='free_codes',
        ),
        migrations.DeleteModel(
            name='telegram_bot',
        ),
        migrations.DeleteModel(
            name='Web_sites',
        ),
    ]
