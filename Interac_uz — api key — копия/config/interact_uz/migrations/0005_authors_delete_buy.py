# Generated by Django 4.1.6 on 2023-12-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interact_uz', '0004_web_sites_link_alter_web_sites_about_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
    ]
