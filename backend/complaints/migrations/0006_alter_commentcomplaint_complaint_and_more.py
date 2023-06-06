# Generated by Django 4.1.7 on 2023-04-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0005_remove_commentcomplaint_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcomplaint',
            name='complaint',
            field=models.CharField(choices=[], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='commentcomplaint',
            name='complaint_status',
            field=models.CharField(choices=[['in_process', 'Жалоба на рассмотрении'], ['done', 'Жалоба рассмотрена'], ['not substantiated', 'Жалоба не обоснована']], default='in_process', max_length=200, verbose_name='Статус жалобы'),
        ),
        migrations.AlterField(
            model_name='groupcomplaint',
            name='complaint',
            field=models.CharField(choices=[], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='groupcomplaint',
            name='complaint_status',
            field=models.CharField(choices=[['in_process', 'Жалоба на рассмотрении'], ['done', 'Жалоба рассмотрена'], ['not substantiated', 'Жалоба не обоснована']], default='in_process', max_length=200, verbose_name='Статус жалобы'),
        ),
        migrations.AlterField(
            model_name='postcomplaint',
            name='complaint',
            field=models.CharField(choices=[], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='postcomplaint',
            name='complaint_status',
            field=models.CharField(choices=[['in_process', 'Жалоба на рассмотрении'], ['done', 'Жалоба рассмотрена'], ['not substantiated', 'Жалоба не обоснована']], default='in_process', max_length=200, verbose_name='Статус жалобы'),
        ),
    ]