# Generated by Django 4.2.5 on 2023-10-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btlgd', '0003_rename_contact_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]