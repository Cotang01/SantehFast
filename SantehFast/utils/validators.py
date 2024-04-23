from django.core.exceptions import ValidationError
import re


PHONE_NUMBER_PATTERN = r'^(?:\+7|8)\d{10}$'


def phone_number_validator(phone: str):
    if not re.match(PHONE_NUMBER_PATTERN, phone):
        raise ValidationError(f'Недопустимый номер телефона: {phone}')
