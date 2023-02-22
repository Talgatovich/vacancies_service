### Vacancies. Тестовое задание
#### API для сервиса с вакансиями

---
###### P.S. Шаблоны для фронта в процессе разработки

---

#### Локальный запуск проекта

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

#### Собрать статические файлы в STATIC_ROOT

```
python3 manage.py collectstatic --noinput
```

#### Создать суперпользователя Django

```
python3 manage.py createsuperuser
```

#### Запустить проект

```
python3 manage.py runserver
```
---
Документация доступна по адресам

<http://127.0.0.1:8000/swagger/> 

<http://127.0.0.1:8000/redoc/> 

---






Автор: [Ибятов Раиль](https://github.com/Talgatovich)
