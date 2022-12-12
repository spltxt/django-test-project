# Django-pizza

Сайт пиццерии на Django.

### Технологии:
- Django 4.0
- Python 3.10
- Celery 5.2.7
- Redis 4.3.4
- PostgreSQL

### Установка и развертывание контейнеров (Docker compose) ###

Если у вас установлен docker-compose (https://docs.docker.com/compose/)

```
* $ git clone https://github.com/spltxt/django-test-project.git

* $ docker-compose up -d
```

Миграции и создание суперпользователя пройдут автоматически.

Чтобы протестировать функционал, перейдите на localhost:8000/admin и войдите, используя следующие данные:
* email - admin@email.com
* password - admin

### Реализовано:
- Как class based, так и function based представления.
- Список товаров, создание и удаление товаров, их детальный просмотр, отзывы и фильтрация по среднему рейтингу товара.
- Профиль пользователя, загрузка изображения профиля.
- Кастомная модель пользователя, кастомная валидация.
- Формирование заказа через формсеты.
- Создание отчёта о продажах и визуализация данных с помощью pandas и seaborn.
- Периодические задачи с celery и celery-beat.
- Тесты с pytest.
- Фронт на django templates.
