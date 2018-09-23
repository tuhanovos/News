from django.contrib import admin

# Register your models here.
from blog.models import CategoriesArticles, Article, Comments


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'news_image', 'categories_article', 'score', 'author', 'news_date']
    ordering = ['title']
    inlines = [ArticleInline]


admin.site.register(Article, AdminArticle)
admin.site.register(CategoriesArticles)
