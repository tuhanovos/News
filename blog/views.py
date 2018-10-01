from allauth.account.forms import LoginForm
from allauth.account.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.core.files.uploadhandler import FileUploadHandler
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from blog.models import Article, CategoriesArticles, Comments
from .forms import RegisterFormView, ProfileForm, LoginFormView, CommentForm

# Create your views here.

"""
Главная страница блога
"""


def index(request):
    if request.method == 'GET':
        news = Article.objects.all().order_by('-news_date')
        return render(request, 'index.html', {'news': news})
    return HttpResponse(status=405)


"""
Регистрация пользователя
"""


def register_user(request):
    if request.method == 'POST':
        form = RegisterFormView(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/add_post')
    else:
        form = RegisterFormView()
    return render(request, 'register_form.html', {'form': form})


"""
Авторизация пользователя
"""


class MyLoginForm(LoginView):
    template_name = 'login.html'


"""
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                my_pass = form.cleaned_data.get('password')
                user = authenticate(email=email, password=my_pass)
                print(form)
                if user:
                    login(request, user)
                    return redirect('index')
        else:
            form = LoginFormView()
        return render(request, 'login.html', {'login_form': form})

"""

"""Выход из профиля"""


def logout_user(request):
    logout(request)
    return redirect('index')


"""
Добавление поста
"""


def user_add_news(request):
    if request.user.is_authenticated:  # Если пользователь аутефицирован добавляем пост
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']  # Заголовок поста
                text = form.cleaned_data['text']  # Текст поста
                category = form.cleaned_data['categories_article']  # Имя категории
                category_id = CategoriesArticles.objects.get(id=category)  # Выбор id категории
                image = form.cleaned_data['image']  # Изображение поста для вывода в списке записей блога
                news = Article(title=title,
                               description=text,
                               categories_article=category_id,
                               news_image=image)  # Передача получегых из формы значений модели.
                # Для записи в базу данных
                try:
                    FileUploadHandler(request.FILES['image'])  # Загрузка изображение на сервер
                except MultiValueDictKeyError:
                    pass
                news.save()
                return redirect('/')
            return redirect('/')
        else:
            form = ProfileForm()
            return render(request, 'blog/add_post.html', {'form': form})
    else:
        return redirect('/login')


"""
Вывод отдельного поста
"""


def view_one_post(request, article_id):
    comments = Comments.objects.filter(comment_article=article_id)
    for comment in comments:
        print(comment.comment_text)
    post = Article.objects.get(pk=article_id)
    Article.objects.filter(id=article_id).update(score=F('score') + 1)
    form_comments = CommentForm
    context = {
        'post': post,
        'comments': comments,
        'form_comments': form_comments,
    }

    return render(request, 'blog/post.html', context)


"""Добавление комментария к статье"""


def add_comment(request, article_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
        return HttpResponseRedirect(f'/blog/post/{article_id}/')
