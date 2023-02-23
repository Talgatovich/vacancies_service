### Vacancies. Тестовое задание
#### API для сервиса с вакансиями

---
###### P.S. Шаблоны для фронта в процессе разработки

---

#### Локальный запуск проекта

#### 1. Через образ Docker
```
docker run --name job_container -it -p 8000:8000 talgatovich/job:v1
```
##### Введите в адресную строку браузера localhost:8000/api/: приложение запущено и работает!

---
#### 2. Не используя Docker

Клонировать репозиторий:

```
git clone git@github.com:Talgatovich/vacancies_service.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Перейти директорию с файлом settings.py

#### Создать файл .env и добавить туда

```
DJANGO_SECRET_KEY=<Приватный ключ Django>

```

Перейти в директорию с файлом manage.py

Выполнить миграции:

```
python3 manage.py migrate
```

#### Создать суперпользователя Django

```
python3 manage.py createsuperuser
```

#### Запустить проект

```
python3 manage.py runserver
```
Перейти по адресу http://127.0.0.1:8000/api/

___


### Проект временно доступен по [ссылке](http://193.107.236.211/api/)

Чтобы войти как соискатель, используйте токен
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjQ3NDU5LCJqdGkiOiJmMGEzOTViOThkZGM0NTk2YmJhYThmZmQ0Njk2MDI5NCIsInVzZXJfaWQiOjEyfQ.EPbUJ2SCy9-nu4PQgrUQrn4bvhNyDPJrhpho2ll1vZ4
```

Чтобы войти как работодатель, используйте токен
``` 
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjQ3ODkwLCJqdGkiOiIzN2U3MGQ1ZjNlM2M0MzdkYTRlYzhiMGI4MzVhODViYyIsInVzZXJfaWQiOjExfQ.7EtTHMcJPo2xWVOHE_KgKG0GNyAlRGhpN61D8RR2ko0
```

---
Документация:

[Swagger](http://193.107.236.211/swagger/)

[Redoc](http://193.107.236.211/redoc/)

---
Доступ к [админке](http://193.107.236.211/admin/):

```
login - admin
password - admin
```
Автор: [Ибятов Раиль](https://github.com/Talgatovich)
