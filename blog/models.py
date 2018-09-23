# coding=utf-8
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

""" 
En: This is the model of the user profile in which he adds the news
Rus: Это модель профиля пользователя в которой он добавляет новость
"""


class CategoriesArticles(models.Model):
    categories_article = models.CharField(
        max_length=100,
        name='categories_article',
        verbose_name='Категории новостей',
        null=True)

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.categories_article


class Article(models.Model):
    title = models.CharField(max_length=100, name='title', verbose_name='Заголовок новости')
    news_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    news_image = models.ImageField(verbose_name='Изображение', null=True, blank=True, upload_to='images/')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Текст новости')
    categories_article = models.ForeignKey(CategoriesArticles,
                                           on_delete=models.CASCADE,
                                           verbose_name='Категория', null=True)
    score = models.PositiveIntegerField(verbose_name='Количество просмотров', name='score', default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_text = models.TextField()
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)