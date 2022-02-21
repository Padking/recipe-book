FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk update && \
    # Установка зависимостей для psycopg2
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/Docker/scripts/entrypoint.sh"]
