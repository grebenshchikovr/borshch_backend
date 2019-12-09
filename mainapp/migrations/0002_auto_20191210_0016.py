# Generated by Django 3.0 on 2019-12-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking',
            field=models.TextField(default=12, verbose_name='способ приготовления'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipe_photos'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='название'),
        ),
    ]
