### Описание:

Yatube API - это проект, который служит для взаимодействия с веб-приоржением Yatube через интерфейс прикладного программирования:

### Установка:

Как развернуть проект на локальной машине?
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Darkteman/api_final_yatube
```

```
cd api_final_yatube
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
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
