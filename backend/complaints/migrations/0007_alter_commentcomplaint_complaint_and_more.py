# Generated by Django 4.1.7 on 2023-04-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0006_alter_commentcomplaint_complaint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcomplaint',
            name='complaint',
            field=models.CharField(choices=[['drugs', 'содержит пропаганду наркотиков'], ['child pornography', 'Публикация содержит детскую порнография']], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='groupcomplaint',
            name='complaint',
            field=models.CharField(choices=[['drugs', 'содержит пропаганду наркотиков'], ['child pornography', 'Публикация содержит детскую порнография']], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='postcomplaint',
            name='complaint',
            field=models.CharField(choices=[['drugs', 'содержит пропаганду наркотиков'], ['child pornography', 'Публикация содержит детскую порнография']], max_length=200, verbose_name='Жалоба'),
        ),
    ]
