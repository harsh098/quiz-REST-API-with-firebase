# Generated by Django 3.2.5 on 2022-08-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_active',
        ),
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active Status'),
        ),
    ]
