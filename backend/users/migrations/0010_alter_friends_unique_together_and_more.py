# Generated by Django 4.1.7 on 2023-05-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_friends_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='friends',
            name='application_status',
            field=models.CharField(choices=[('approved', 'заявка принята'), ('pending', 'заявка в ожидании')], default='pending', max_length=20),
        ),
    ]
