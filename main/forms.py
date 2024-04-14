from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите логин '}))
    name = forms.CharField(max_length= 22, label = 'Имя и Фамилия', widget = forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите имя и фамилию '}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль еще раз '}))

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль'}))
    

class TestForm(forms.Form): 
    CHOICES_Q1 =( 
    ("1", "abcdef"), 
    ("2", "pasha_13567"), 
    ("3", "E%mtC3{{aC~I"))

    CHOICES_Q2 =( 
    ("1", "Отключить компьютер от Интернета"), 
    ("2", "Перенести все файлы на внешний накопитель"), 
    ("3", "Проверить банковский счет"))

    CHOICES_Q3 =( 
    ("1", "Удалю письмо. Я ничего не знаю об этом сайте и авторе письма."), 
    ("2", "Перейду по ссылке и получу приз"))

    
    CHOICES_Q4 =( 
    ("1", "Отправлю деньги другу"), 
    ("2", "Уточню, что случилось с другом не через социальную сеть"))

    CHOICES_Q5 =( 
    ("1", "Сообщения в СМИ"), 
    ("2", "Сообщения от классного руководителя"), 
    ("3", "Сообщения на электронную почту"))

    CHOICES_Q6 =( 
    ("1", "Запомнить внешний вид сайтов, которым можно доверять"), 
    ("2", "Установить самую последнюю версию браузера"), 
    ("3", "Внимательно проверять ссылки на сайты и установить хороший антивирус"))

    CHOICES_Q7 =( 
    ("1", "Подключусь. Уже 100 раз так делал(а)"), 
    ("2", "На всякий случай не буду"))


    q1 = forms.MultipleChoiceField(required= False, label = "Какой из предложенных паролей лучше выбрать?", choices= CHOICES_Q1,  widget = forms.CheckboxSelectMultiple())
    q2 = forms.MultipleChoiceField(required= False, label = "Что нужно сделать в первую очередь, если компьютер подвергся атаке?", choices= CHOICES_Q2,  widget = forms.CheckboxSelectMultiple())
    q3 = forms.MultipleChoiceField(required= False, label = "Вам пришло письмо: «Вы выиграли 5 миллионов рублей, вам нужно зарегистрироваться на этом сайте (ссылка на сайт). Регистрация закрывается завтра. Не пропустите!». Что вы сделаете?", choices= CHOICES_Q3,  widget = forms.CheckboxSelectMultiple())
    q4 = forms.MultipleChoiceField(required= False, label = "Ваш друг написал вам следующее сообщение: \"у мeня гoре помoги, дай денег в долг\".  Что вы будете делать?", choices= CHOICES_Q4,  widget = forms.CheckboxSelectMultiple())
    q5 = forms.MultipleChoiceField(required= False, label = "Выберите из перечисленного ниже наиболее часто используемые каналы распространения спама:", choices= CHOICES_Q5,  widget = forms.CheckboxSelectMultiple())
    q6 = forms.MultipleChoiceField(required= False, label = "Выберите из перечисленного ниже правильный способ защиты от фишинга:", choices= CHOICES_Q6,  widget = forms.CheckboxSelectMultiple())
    q7 = forms.MultipleChoiceField(required= False, label = "Вам нужно подключиться к Wi-Fi, но доступна только точка без пароля. Ваши действия:", choices= CHOICES_Q7,  widget = forms.CheckboxSelectMultiple())
    
    