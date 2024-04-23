from django import forms
from .models import Order
from utils.validators import phone_number_validator

REPAIR_CATEGORIES = (
    ('option1', 'Сантехника'),
    ('option2', 'Электрика'),
    ('option3', 'Прочее')
)


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['phone'].initial = user.phone
        else:
            self.fields['phone'] = forms.CharField(max_length=15,
                                                   label='Номер телефона',
                                                   validators=[phone_number_validator])

    full_name = forms.CharField(max_length=50,
                                label='Как к вам обращаться? (Имя Отчество)')
    repair_category = forms.ChoiceField(choices=REPAIR_CATEGORIES,
                                        label='Какой ремонт нужен')
    address = forms.CharField(max_length=100,
                              label='Город, улица, дом, квартира, '
                                    'где нужен ремонт')

    class Meta:
        model = Order
        fields = ['phone', 'full_name', 'repair_category', 'address']


