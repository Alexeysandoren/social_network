# Generated by Django 4.1.7 on 2023-04-25 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_friends_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=set(),
        ),
    ]
