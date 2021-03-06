# Generated by Django 4.0.5 on 2022-07-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='users.car', verbose_name='los carros del usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='El nombre de la persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='El apellido de la persona'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
