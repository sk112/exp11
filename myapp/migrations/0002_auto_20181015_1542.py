# Generated by Django 2.1.2 on 2018-10-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default='No Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=1024),
        ),
    ]