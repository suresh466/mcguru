# Generated by Django 2.2.2 on 2019-07-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20190617_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_num',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]