from django.core.validators import RegexValidator

validate_phone_number = RegexValidator(r'^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$',
                                 message='Пожалуйста, попробуйте ещё раз')
