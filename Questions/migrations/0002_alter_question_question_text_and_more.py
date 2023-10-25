# Generated by Django 4.2.6 on 2023-10-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
