#!/usr/bin/env bash
# wait-for-postgres.sh
set -e
host="$1"
shift
cmd="$@"

# Debug line to see environment variables
echo "Debug: POSTGRES_USER=$POSTGRES_USER, POSTGRES_DB=$POSTGRES_DB"
echo "Debug: Attempting to connect to database '$POSTGRES_DB' as user '$POSTGRES_USER'"

until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>&1; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up - executing command"
exec $cmd