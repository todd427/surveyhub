#!/bin/bash

# Usage: ./prepDocker.sh {prod|drd}

set -e

REQUIRED_KEYS=("SECRET_KEY" "DATABASE_URL")

ENV_NAME=$1
ACTION=$2

if [[ "$ENV_NAME" != "prod" && "$ENV_NAME" != "drd" ]]; then
    echo "Usage: $0 {prod|drd}"
    exit 1
fi

ENV_FILE=".env.$ENV_NAME"

if [[ ! -f "$ENV_FILE" ]]; then
    echo "❌ Environment file $ENV_FILE does not exist!"
    exit 2
fi

# Validate required keys are present and non-empty
for key in "${REQUIRED_KEYS[@]}"; do
    # grep returns the whole line, we extract after the =
    value=$(grep -E "^${key}=" "$ENV_FILE" | cut -d'=' -f2-)
    if [[ -z "$value" ]]; then
        echo "❌ Required key $key is missing or empty in $ENV_FILE!"
        exit 3
    fi
done

# Copy the env file into .env for Docker Compose
cp "$ENV_FILE" .env

export DJANGO_ENV_FILE="$ENV_FILE"
echo "✅ Set DJANGO_ENV_FILE=$ENV_FILE"
echo "✅ .env now points to $ENV_FILE"

echo "All required keys are present."


if [[ "$ACTION" == "up" ]]; then
    echo "Starting containers..."
    docker compose up
fi

if [[ "$ACTION" == "down" ]]; then
    echo "Stopping containers..."
    docker compose down
fi

if [[ "$ACTION" == "restart" ]]; then 
    echo "Restarting containers..."
    docker compose down
    docker compose up
fi

if [[ "$ACTION" == "logs" ]]; then
    echo "Showing logs..."
    docker compose logs -f
fi

if [[ "$ACTION" == "build" ]]; then
    echo "Building containers..."
    docker compose build
fi

if [[ "$ACTION" == "bash" ]]; then
    echo "Opening bash shell..."
    docker compose exec web bash
fi

if [[ "$ACTION" == "shell" ]]; then
    echo "Opening shell..."
    docker compose exec web python manage.py shell
fi