# Generated by Django 4.2.2 on 2023-06-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_rename_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Address',
            field=models.CharField(max_length=255),
        ),
    ]
