# Generated by Django 3.1.6 on 2021-02-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210212_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='visibility',
            field=models.CharField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=10),
            preserve_default=False,
        ),
    ]
