# Generated by Django 4.2.3 on 2023-08-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_online_shop', '0003_onlineshop_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineshop',
            name='image',
        ),
        migrations.AddField(
            model_name='onlineshop',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='post/thumbnail/%Y/%m/%d/'),
        ),
    ]
