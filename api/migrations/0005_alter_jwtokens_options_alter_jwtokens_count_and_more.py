# Generated by Django 4.0.5 on 2022-06-27 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_alter_jwtokens_exp_alter_jwtokens_iat_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jwtokens',
            options={'verbose_name': 'Токен', 'verbose_name_plural': 'Токены'},
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='count',
            field=models.IntegerField(verbose_name='Количество запросов'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='exp',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Время токена'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='iat',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Iat'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='isAdmin',
            field=models.BooleanField(default=False, verbose_name='Является ли админским'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='jti',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Jti'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='minutes',
            field=models.IntegerField(verbose_name='На какой срок был создан токен'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Последний запрос'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='token',
            field=models.CharField(blank=True, editable=False, max_length=1000, null=True, verbose_name='Токен'),
        ),
        migrations.AlterField(
            model_name='jwtokens',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь токена'),
        ),
    ]