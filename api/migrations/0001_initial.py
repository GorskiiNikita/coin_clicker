# Generated by Django 3.0.7 on 2020-07-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VkUsers',
            fields=[
                ('vk_user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('count_clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
