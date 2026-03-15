#!/bin/bash
set -e

echo "🚀 Deploying AdBook Backend..."

REPO_DIR="$(pwd)"
REPO="https://github.com/adylbek1406/backend-adbook.git"

if [ ! -d ".git" ]; then
  echo "Cloning repo..."
  git clone $REPO .
else
  echo "Pulling latest..."
  git pull origin main
fi

# Env setup
if [ ! -f .env ]; then
  echo "Copying .env.example to .env (EDIT DB CREDS etc. before running!)"
  cp .env.example .env
  echo "⚠️  Edit .env now: $REPO_DIR/.env"
  exit 1
fi

# Docker compose up
echo "Starting Docker services..."
docker compose down || true
docker compose pull
docker compose up -d --build

# Wait for healthy
echo "Waiting for services..."
sleep 30

# Migrations
docker compose exec -T backend python manage.py migrate --noinput

# Collect static (if not in Dockerfile)
docker compose exec backend python manage.py collectstatic --noinput || true

echo "✅ Deploy complete!"
echo "🌐 Server: http://$(hostname -I | awk '{print $1}'):80"
echo "📊 Logs: docker compose logs -f"
echo "🔍 Health: curl http://localhost/health/"

