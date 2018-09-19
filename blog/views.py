
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.uploadhandler import FileUploadHandler
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from blog.models import UserCreateNews, CategoriesNews
from .forms import RegisterFormView, ProfileForm

# Create your views here.

"""
Главная страница блога
"""


def index(request):
    if request.method == 'GET':
        news = UserCreateNews.objects.all().order_by('-news_date')
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
    return render(request, 'login.html', {'form': form})


"""
Авторизация пользователя
"""


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                my_pass = form.cleaned_data.get('password')
                user = authenticate(username=username, password=my_pass)
                login(request, user)
                return redirect('/blog')
        else:
            form = AuthenticationForm()
        return render(request, 'register_form.html', {'form': form})


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
                category = form.cleaned_data['categories_news']  # Имя категории
                category_id = CategoriesNews.objects.get(id=category)  # Выбор id категории
                image = form.cleaned_data['image']  # Изображение поста для вывода в списке записей блога
                news = UserCreateNews(title=title,
                                      description=text,
                                      categories_news=category_id,
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


def view_one_post(request, news_id):
    post = UserCreateNews.objects.get(pk=news_id)
    UserCreateNews.objects.filter(id=news_id).update(score=F('score') + 1)
    return render(request, 'blog/post.html', {'post': post})
