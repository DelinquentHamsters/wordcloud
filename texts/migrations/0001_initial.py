# Generated by Django 2.0.2 on 2018-05-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publishe', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/')),
                ('body', models.TextField()),
            ],
        ),
    ]
