# Recipe Book

Сайт-книга рецептов

## Описание

Интерактивная таблица рецептов блюд


### Особенности

- помогает составить рацион питания,
- предоставляет возможность:
    * создать/редактировать рецепты,
    * поиска рецепта и/или ингредиента по названию,
    * просмотра рецепта(ов).
- статус проекта: учебный.

## Пример работы


![demo](screenshots/demo.gif)


### Используемые технологии

* [Django](https://docs.djangoproject.com/en/3.1/)
* [Docker](https://docs.docker.com/engine/)
* [Docker Compose](https://docs.docker.com/compose/)
* [PostgreSQL](https://postgrespro.ru/docs/postgresql/14/index)

## Требования к окружению

* Python 3.8 и выше,
* Linux/Windows,
* Переменные окружения (ПеО),
* Файлы для системы виртуализации (СВ).

Проект настраивается через ПеО, достаточно задать их в файлах `.env.override` и `.env.override.db`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты | - |
|`DEBUG`| Режим отладки | `True` |
|`SECRET_KEY`| Уникальное непредсказуемое значение | - |
|`STATIC_ROOT`| Имя каталога с статикой проекта |`static`|
|`STATIC_URL`| Имя path-части URL для отдачи статики |`/static/`|
|`MEDIA_ROOT`| Имя каталога с медиа-файлами проекта |`media`|
|`MEDIA_URL`| Имя path-части URL для отдачи медиа-файлов |`/media/`|
|`PSQL_DB_ENGINE`| Имя движка СУБД |`django.db.backends.postgresql`|
|`PSQL_DB_HOST`| Имя сервиса развёрнутого в контейнере для БД | `db` |
|`PSQL_DB_PORT`| Порт СУБД | `5432` |
|`PSQL_DB_NAME`| Имя БД | `recipe_book` |
|`PSQL_DB_USER`| Имя пользователя БД | `proba` |
|`PSQL_DB_PASSWORD`| Пароль пользователя БД | `proba` |

### Параметры подключения к БД

По умолчанию используется СУБД PostgreSQL.

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`POSTGRES_USER`| Суперпользователь БД | `postgres` |
|`POSTGRES_PASSWORD`| Пароль суперпользователя БД | `postgres` |


### Организация dev-среды

- создать на основе `env.override` и `env.override.db` файлы `env` и `env.db`,
- заполнить значениями ключи, у которых нет значений по умолчанию.

## Установка

1. Клонировать проект:
```sh
git clone https://github.com/Padking/recipe-book.git
cd recipe-book
```
2. [Установить и настроить](https://docs.docker.com/engine/install/) Docker,
3. [Установить и настроить](https://docs.docker.com/compose/install/) Docker Compose,
4. Собрать образы для сервисов проекта,
   запустить контейнеры с сервисами в фоновом режиме:
```sh
docker-compose build
docker-compose up -d
```
5. Применить миграции к проекту:
```sh
docker-compose exec web python manage.py migrate --noinput
```
6. Собрать статику для проекта:
```sh
docker-compose exec web python manage.py collectstatic --clear
```
7. Применить фикстуру
```sh
docker-compose exec web python manage.py loaddata ./recipes/fixtures/db_data.json
```

8. Запустить [сайт](http://127.0.0.1:8000/),

9. Cоздать суперпользователя в интерактивном режиме*:
```sh
docker-compose exec web python manage.py createsuperuser
```
10.  Завершить работу сайта:
```sh
docker-compose down
```

\* для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
