# Generated by Django 3.0.3 on 2020-03-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('votes_total', models.IntegerField(default=0)),
            ],
        ),
    ]
