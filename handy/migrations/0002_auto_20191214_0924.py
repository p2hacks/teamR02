# Generated by Django 3.0 on 2019-12-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='clab',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='egg',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='milk',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='peanuts',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='shrimp',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='soba',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='wheat',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]