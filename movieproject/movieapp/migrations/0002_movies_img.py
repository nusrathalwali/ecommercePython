# Generated by Django 4.2.8 on 2023-12-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='dddddf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
