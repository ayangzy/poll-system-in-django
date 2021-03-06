# Generated by Django 3.0.3 on 2020-03-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='user_id',
            field=models.IntegerField(blank=True, default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contestant',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
