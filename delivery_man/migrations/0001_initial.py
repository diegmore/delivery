# Generated by Django 4.1 on 2022-10-22 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.IntegerField()),
                ('long', models.IntegerField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
    ]