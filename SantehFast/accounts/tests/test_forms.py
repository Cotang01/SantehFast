from django.test import TestCase
from parameterized import parameterized

from ..forms import UserRegisterForm


# cmd ['python', 'manage.py', 'test'] doesn't see nested classes, so both
# objects are declared under single setUp function
class UserRegisterFormTest(TestCase):

    def setUp(self) -> None:
        self.valid_form = {
            'username': 'testusername',
            'phone': '+71234567890',
            'email': 'example@mail.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        }

        self.invalid_form = {
            'username': 'mytestusername123@@@',
            'phone': '+71234567890d',
            'email': 'examplemail.com',
            'password1': 'TestPaswdsaasd',
            'password2': 'TestPasswordd123'
        }

    def test_form_valid(self):
        form = UserRegisterForm(data=self.valid_form)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = UserRegisterForm(data=self.invalid_form)
        self.assertFalse(form.is_valid())

    def test_form_invalid_phone(self):
        form = UserRegisterForm(data=self.invalid_form)
        inv_phone = self.invalid_form['phone']
        self.assertIn('phone', form.errors)
        self.assertFormError(form, 'phone',
                             f'Недопустимый номер телефона: {inv_phone}')

    def test_form_invalid_password_mismatch(self):
        form = UserRegisterForm(data=self.invalid_form)
        self.assertIn('password2', form.errors)
        self.assertFormError(form, 'password2',
                             'Введенные пароли не совпадают.')

