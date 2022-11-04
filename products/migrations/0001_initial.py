# Generated by Django 4.1.3 on 2022-11-04 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subname', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]
