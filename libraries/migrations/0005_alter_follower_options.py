# Generated by Django 4.0.5 on 2022-06-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0004_follower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'verbose_name': 'Подписчики на рассылку', 'verbose_name_plural': 'Подписчики на рассылку'},
        ),
    ]