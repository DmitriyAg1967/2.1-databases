# Generated by Django 3.1.2 on 2022-04-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.TextField()),
                ('image', models.TextField()),
                ('release_date', models.TextField()),
                ('lte_exists', models.TextField()),
                ('slug', models.TextField()),
            ],
        ),
    ]
