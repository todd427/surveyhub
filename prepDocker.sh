#!/bin/bash

# prepDocker.sh

# One-command prep for running your Django project with Docker Compose.
#
# Copies the selected .env file to .env and exports DJANGO_ENV_FILE accordingly.
# Ensures required variables exist. Fails if a key is missing.
#
# ACTIONS:
#   prod            Use production config      (.env.prod)
#   drd             Use debug/Dr. Debug config (.env.drd)
#   local           Use local dev config      (.env.local)
#   custom <name>   Use custom env file       (.env.<name>)
#   up              Start containers (docker compose up)
#   down            Stop containers (docker compose down)
#   restart         Restart containers
#   logs            Show container logs
#   build           Build containers
#   bash            Open bash shell in web container
#   shell           Open Django shell in web container
#   help            Show this usage message

show_usage() {
    echo ""
    echo "Usage: $0 {prod|drd|local|custom <NAME>|up|down|restart|logs|build|bash|shell|help}"
    echo ""
    echo "ENV:"
    echo "  prod            Use .env.prod   (sets DJANGO_ENV_FILE=.env.prod)"
    echo "  drd             Use .env.drd    (sets DJANGO_ENV_FILE=.env.drd)"
    echo "  local           Use .env.local  (sets DJANGO_ENV_FILE=.env.local)"
    echo "  custom <NAME>   Use .env.<NAME> (sets DJANGO_ENV_FILE=.env.<NAME>)"
    echo ""
    echo "ACTIONS:"
    echo "  up              Start containers        (docker compose up)"
    echo "  down            Stop containers         (docker compose down)"
    echo "  restart         Restart containers      (docker compose down; up)"
    echo "  logs            Show container logs     (docker compose logs -f)"
    echo "  build           Build containers        (docker compose build)"
    echo "  bash            Bash shell in web       (docker compose exec web bash)"
    echo "  shell           Django shell in web     (docker compose exec web python manage.py shell)"
    echo ""
    echo "  help            Show this help/usage message"
    echo ""
    echo "Fails if the selected .env file does not exist or is missing required keys."
    echo ""
    echo "Examples:"
    echo "  $0 prod"
    echo "  $0 drd"
    echo "  $0 custom staging"
    echo "  $0 up"
    echo "  $0 logs"
    echo ""
}


ENV=${1:-help}
ACTION=${2:-help}

case "$ENV" in
    prod)
        FILE=".env.prod"
        ;;
    drd)
        FILE=".env.drd"
        ;;
    local)
        FILE=".env.local"
        ;;
    custom)
        if [ $# -lt 2 ]; then
            echo "❌ Custom env file name required, e.g., ./$0 custom foo"
            show_usage
            exit 2
        fi
        FILE=".env.$2"
        ;;
    up|down|restart|logs|build|bash|shell)
        # Defer .env prep for non-env actions
        ;;
    help|*)
        show_usage
        exit 1
        ;;
esac

REQUIRED="SECRET_KEY DATABASE_URL"

if [[ "$ENV" =~ ^(prod|drd|local|custom)$ ]]; then
    if [ ! -f "$FILE" ]; then
        echo "❌ $FILE does not exist."
        exit 2
    fi
    for key in $REQUIRED; do
        if ! grep -q "^$key=" "$FILE"; then
            echo "❌ $key is missing from $FILE"
            exit 3
        fi
    done
    cp "$FILE" .env
    export DJANGO_ENV_FILE="$FILE"
    echo "✅ Copied $FILE to .env and exported DJANGO_ENV_FILE=$FILE"
fi

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
    echo "Opening Django shell..."
    docker compose exec web python manage.py shell
fi