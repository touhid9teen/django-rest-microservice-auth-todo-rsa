# Generated by Django 5.1 on 2024-09-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
