# Generated by Django 2.1.7 on 2019-06-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20190615_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='hint',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='right_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='total_right_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='total_wrong_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='wrong_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
