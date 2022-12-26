# Generated by Django 4.1.1 on 2022-12-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=20, null=True)),
                ('materials', models.TextField()),
            ],
        ),
    ]