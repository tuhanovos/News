# Generated by Django 2.1 on 2018-09-23 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.CategoriesArticles', verbose_name='Категория'),
        ),
    ]