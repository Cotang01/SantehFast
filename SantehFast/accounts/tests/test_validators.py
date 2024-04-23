from django.test import TestCase
from django.core.exceptions import ValidationError
from parameterized import parameterized

from utils.validators import phone_number_validator


class AccountValidatorsTest(TestCase):

    @parameterized.expand(
        ['+71234567890', '89876543210', '88005553535']
    )
    def test_phone_number_validator_success(self, case: str):
        phone_number_validator(case)

    @parameterized.expand(
        ['71234567890', '19876543210', '',
         '082309843', 'ubyubq23v3', '-70987123456']
    )
    def test_phone_number_validator_raises(self, case: str):
        with self.assertRaises(ValidationError,
                               msg=f'Недопустимый номер телефона: {case}'):
            phone_number_validator(case)
