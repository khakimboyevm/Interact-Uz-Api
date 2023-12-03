# Generated by Django 4.1.6 on 2023-11-22 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interact_uz', '0002_web_sites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('suit_price', models.TextField(max_length=50)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interact_uz.web_sites')),
            ],
        ),
    ]
