# Generated by Django 4.2.2 on 2023-06-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_remove_message_full_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Email_Address',
            field=models.EmailField(max_length=255),
        ),
    ]