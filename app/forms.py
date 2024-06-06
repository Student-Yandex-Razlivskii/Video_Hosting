"""
Definition of forms.
"""

from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Blog, Comment


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class Comments(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш рол',
        choices=[('1', 'Мужской'), ('2', "Женский")],
        widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label=" Оцените наш видео контент",
        choices=(("1", "Отлично"),
        ("2", "Хорошо"),
        ("3", "Неплохо"),
        ("4", 'Плохо')), initial=1)
    notice = forms.BooleanField(label="Получать новости сайта на e-mail?",
        required=False)
    email = forms.EmailField(label="Ваш e-mail", min_length=7)
    message = forms.CharField(label='Ваши пожелания по улучшению нашего сайта',
        widget=forms.Textarea(attrs={'rows' :12, 'cols':20}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image', 'video',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка", 'video': "Видео"}
