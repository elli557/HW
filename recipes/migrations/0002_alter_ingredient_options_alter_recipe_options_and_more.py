# Generated by Django 5.2 on 2025-05-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'ингредиент', 'verbose_name_plural': 'ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'рецепт', 'verbose_name_plural': 'рецепты'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название ингредиента'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=100, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Описание рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название рецепта'),
        ),
    ]
