from django.core.validators import RegexValidator

# phone number validator
validate_phone_number = RegexValidator(r'^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$',
                                 message='Некорректный номер телефона, попробуйте ещё раз')
