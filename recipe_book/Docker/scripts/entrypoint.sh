#!/bin/sh

set -o errexit
set -o nounset

postgres_ready() {
python << END
import os
import sys

import psycopg2

try:
    conn = psycopg2.connect(
        dbname=os.environ['PSQL_DB_NAME'],
        user=os.environ['PSQL_DB_USER'],
        password=os.environ['PSQL_DB_PASSWORD'],
        host=os.environ['PSQL_DB_HOST'],
        port=os.environ['PSQL_DB_PORT'],
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres ${PSQL_DB_HOST}:${PSQL_DB_PORT}/${PSQL_DB_NAME} is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."


exec "$@"
