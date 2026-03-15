# AdBook Backend

Instagram-like social platform for book lovers. Share reviews, build collections, chat about reads, follow authors/users.

## Features
- 📚 Book catalog + reviews + full-text search (PostgreSQL)
- 📱 Posts/Images/Likes/Comments/Follows (Instagram-style feed)
- 💬 Real-time chat (Channels/WebSockets)
- 🔔 Push notifications (Celery)
- 🔐 Auth: Email/Phone/OTP + JWT (Redis blacklist)
- ⚡ Scale: Redis cache, Celery workers, Docker-compose, Pg indexes/partitioning
- 📊 API: DRF + Swagger (OpenAPI), 1M user optimized

## Tech Stack
```
Backend: Django 5 + DRF + Celery + Channels
DB: PostgreSQL 16 (GIN search, partitioning)
Cache/Broker: Redis 7
Server: Gunicorn/Uvicorn + Nginx
DevOps: Docker Compose
```
ER Diagram: [ER_DIAGRAM.md](ER_DIAGRAM.md)

## Quick Start
```bash
cp .env.example .env  # Edit secrets
docker compose up --build
docker compose exec backend python manage.py createsuperuser
# API: http://localhost/api/v1/
# Docs: http://localhost/api/v1/schema/swagger-ui/
```

## API Endpoints (Phase 3+)
- `/api/v1/auth/` - Register/Login/OTP
- `/api/v1/books/` - CRUD + search
- `/api/v1/posts/` - Feed + social
- `/api/v1/chat/` - WebSocket rooms

## Scaling (Prod)
- PgBouncer + Read Replicas
- Celery Flower monitoring
- Redis Cluster
- New Relic/Sentry

## Development
```bash
# Migrations
docker compose exec backend python manage.py makemigrations && migrate

# Tests
docker compose exec backend pytest

# Shell
docker compose exec backend python manage.py shell_plus
```

See TODO.md for progress.
