# Generated by Django 3.0.1 on 2020-09-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('realname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
