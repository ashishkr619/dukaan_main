# Generated by Django 2.2.17 on 2021-01-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20210111_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='store_link',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='unique Store Link'),
        ),
    ]