import datetime as dt
import re
from django.core.exceptions import ValidationError


def validate_year(year):
    if year > dt.datetime.now().year:
        raise ValueError(f'Некорректный год {year}')


def validate_username(name):
    if name == 'me':
        raise ValidationError('Имя пользователя "me" использовать запрещено!')
    if not re.compile(r'^[\w.@+-]+').fullmatch(name):
        raise ValidationError(
            'Можно использовать только буквы, цифры и символы @.+-_".')


def validate_genre(genre):
    if genre == '':
        raise ValidationError(
            'Поле "Genre" должно быть заполнено',
        )
