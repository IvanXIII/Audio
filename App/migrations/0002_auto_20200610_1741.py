# Generated by Django 3.0.7 on 2020-06-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название лекции')),
                ('number_of_lection', models.IntegerField(verbose_name='Номер лекции')),
                ('description', models.TextField(verbose_name='Краткое описание лекции')),
                ('short_description', models.CharField(max_length=50, verbose_name='Очень краткое описание лекции')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]