# Generated by Django 4.0 on 2021-12-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0002_rename_title_review_titler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='titleR',
            field=models.CharField(max_length=128, verbose_name='titre'),
        ),
    ]
