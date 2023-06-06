# Generated by Django 4.1.7 on 2023-05-04 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_alter_friends_unique_together'),
        ('complaints', '0008_alter_commentcomplaint_complaint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(choices=[['in_process', 'Жалоба на рассмотрении'], ['done', 'Жалоба рассмотрена'], ['not substantiated', 'Жалоба не обоснована']], default='in_process', max_length=200, verbose_name='Статус жалобы')),
                ('complaint', models.CharField(choices=[('clone', 'Пользователь копирует ваши фото и информацию и пытается выдать себя за вас'), ('child pornography', 'В профиле содержится детская порнография'), ('spam', 'Пользователь рассылает рекламные сообщения, комментарии или другим способом распространяет рекламу в не предназначенных для этого местах.')], max_length=200, verbose_name='Жалоба')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Профиль на который поступила жалоба')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь оставивший жалобу')),
            ],
            options={
                'verbose_name': 'Жалоба на профиль',
                'verbose_name_plural': 'Жалобы на профиль',
            },
        ),
    ]