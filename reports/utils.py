import base64
import uuid
from django.core.files.base import ContentFile


def get_report_image(data):
    """
    Создание картинки для отчёта
    """
    _, str_image = data.split(';base64')
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + '.png'
    data = ContentFile(decoded_img, name=img_name)
    return data


def is_ajax(request) -> bool:
    """
    Чек, является ли аджакс запросом
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
