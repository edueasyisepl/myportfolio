# Generated by Django 4.2.2 on 2023-06-30 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_alter_message_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Address',
            new_name='Full_Address',
        ),
    ]
