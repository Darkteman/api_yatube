### Описание:

Yatube API - это проект, который служит для взаимодействия с веб-приоржением Yatube через интерфейс прикладного программирования:

### Установка:

Как развернуть проект на локальной машине?
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Darkteman/api_yatube
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры:

Некоторые примеры запросов к API:

```
http://127.0.0.1:8000/api/v1/posts/
```
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=40&limit=10",
    "previous": "http://api.example.org/accounts/?offset=20&limit=10",
    "results": [
        {
            "id": 1,
            "author": "admin",
            "text": "Первый пост админа",
            "pub_date": "2022-11-01T23:28:35.860669Z",
            "image": null,
            "group": 1
        }
    ]
}
```
```
http://127.0.0.1:8000/api/v1/posts/1/comments/1
```
```
{
    "id": 1,
    "author": "admin",
    "text": "Комментарий админа к 1му посту.",
    "created": "2022-11-02T08:22:41.941046Z",
    "post": 1
}

```
```
http://127.0.0.1:8000/api/v1/follow/
```
```
{
    "user": "admin"
    "following": "user2"
}
