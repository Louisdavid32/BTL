# Generated by Django 4.2.5 on 2023-10-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btlgd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('phonenb', models.IntegerField()),
                ('des', models.TextField(blank=True)),
                ('dpt', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
