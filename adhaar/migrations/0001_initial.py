# Generated by Django 3.0.2 on 2020-01-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaar_number', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]