# Generated by Django 5.2.1 on 2025-05-27 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-update_at',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
