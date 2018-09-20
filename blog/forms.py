from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import FormView

from blog.models import CategoriesNews

"""
Форма регистрации пользователя на сайте
"""


class RegisterFormView(UserCreationForm):
    username = forms.CharField(max_length=30, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'placeholder': ''}))

    email = forms.EmailField(max_length=254,
                             help_text='Это поле обязательно', widget=forms.TextInput(attrs={'placeholder': ''}))

    address = forms.CharField(max_length=100,
                              help_text='Укажите ваш город',
                              label='Ваш адрес', widget=forms.TextInput(attrs={'placeholder': ''}))

    password1 = forms.CharField(label="Пароль",
                                strip=False,
                                widget=forms.PasswordInput(attrs={'placeholder': ''}),
                                help_text='Введите ваш пароль')

    password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput(attrs={'placeholder': ''}),
                                help_text='Повторите пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'password1', 'password2',)


"""Форма авторизации"""


class LoginFormView(forms.Form):
    email = forms.EmailField(label='Введите email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}), label='Введите пароль')

    def __init(self):
        super(forms.Form, self).__init__(self)
        del self.fields['username']


"""
Форма добавления новости в блог
"""


class ProfileForm(forms.Form):
    CHOICES = CategoriesNews.objects.all().values_list('id', 'categories_news')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}), max_length=150,
                            label='Заголовок новости')
    categories_news = forms.ChoiceField(choices=CHOICES, label='Выберите категорию')
    text = forms.CharField(widget=CKEditorUploadingWidget(config_name='default'), label='Текст новости')
    image = forms.ImageField(label='Загрузить изображение', required=False)
