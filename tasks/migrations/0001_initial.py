# Generated by Django 4.2.6 on 2023-11-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default='', max_length=200)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]