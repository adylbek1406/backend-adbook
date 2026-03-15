# AdBook Backend 🚀

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED)](https://www.docker.com/)

**AdBook** - Production-grade Instagram-like social platform for **books**, scaling to **1M users**.

## ✨ Features
- 📚 Books catalog + reviews
- 📱 Posts, comments, likes
- 👥 Followers/subscriptions
- 💬 Real-time chat (WebSockets)
- 🔔 Push notifications (WebSockets)
- 🎯 Personalized feed
- 🔍 Full-text search (PostgreSQL)
- 🔐 Advanced auth: JWT, OTP, 2FA, device tracking
- ⚡ Scalable: Redis cache, Celery tasks, read replicas ready

## 🏗️ Architecture
```
Clean Architecture | 12 Modular Django Apps:
├── accounts (Auth + Profiles)
├── books          | posts (w/ images)
├── comments       | likes
├── subscriptions  | collections
├── notifications  | chat (Channels)
├── feed           | search
└── core (Shared)
```
**ER Schema**: 20+ tables w/ optimized indexes.

## 🚀 Quick Start (Docker)

### 1. Clone & Setup
```bash
cd /Users/adylbek/Desktop/backend_adbook/adbook-backend
cp .env.example .env
# Edit .env: DATABASE_PASSWORD=1406
```

### 2. Launch
```bash
docker-compose up --build
# Backend: http://127.0.0.1:8000
# Admin: http://127.0.0.1:8000/admin/
```

### 3. Migrations & Superuser
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

### 4. API Base
```
Authorization: Bearer YOUR_JWT_TOKEN
Base URL: http://127.0.0.1:8000/api/v1/
Docs: /api/v1/schema/swagger-ui/ (DRF-Spectacular)
```

**Auth Flow**:
```bash
# Register
curl -X POST http://127.0.0.1:8000/api/v1/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "pass123", "name": "User"}'

# Login
curl -X POST http://127.0.0.1:8000/api/v1/accounts/login/ \
  -d '{"email": "user@example.com", "password": "pass123"}'
```

### 5. Key Endpoints
```
GET  /api/v1/posts/                    # Personalized feed
POST /api/v1/posts/                    # Create post
GET  /api/v1/feed/                     # Global feed
WS   ws://127.0.0.1:8000/ws/chat/1/    # Chat room
GET  /api/v1/search/?q=python          # Full-text search
```

## 🔧 Production Deployment (Linux Server)
```bash
# 1. Build & push images
docker-compose -f docker-compose.prod.yml build
docker push your-registry/adbook-backend:latest

# 2. Deploy
ssh user@prod-server
docker-compose -f docker-compose.prod.yml up -d

# 3. Scaling
docker-compose up -d --scale backend=4 worker=2
```

## 📊 Scalability (1M Users)
- **Horizontal**: Gunicorn 4+ workers, Nginx LB
- **DB**: PostgreSQL read replicas + PgBouncer
- **Cache**: Redis Cluster
- **Media**: S3 + CDN (CloudFront ready)
- **Async**: Celery distributed tasks
- **Monitoring**: Ready for Prometheus/Grafana

## 🛠️ Local Development
```bash
# Dev mode (hot reload)
docker-compose -f docker-compose.dev.yml up

# Run tests
docker-compose exec backend pytest

# Celery worker
docker-compose up worker

# Channels dev server
docker-compose exec backend python manage.py runserver 0.0.0.0:8000
```

## 📄 API Documentation
Auto-generated Swagger: `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`

## 🔒 Security
- ✅ JWT + Redis token blacklist
- ✅ Rate limiting + throttling
- ✅ CORS/CSRF protection
- ✅ SQL/XSS injection safe
- ✅ HTTPS ready (Let's Encrypt)

## 🏷️ Tech Stack
```
Backend: Django 5 + DRF + Channels 4
DB: PostgreSQL 16 + Redis 7
Queue: Celery 5.4
Server: Gunicorn 22 + Nginx 1.26
Infra: Docker Compose + S3
Search: PostgreSQL GIN/Full-Text
```

## 🤝 Contributing
1. Fork → Clone → `docker-compose up`
2. Create feature branch: `git checkout -b feature/books-api`
3. PR to `develop` branch

## 📞 Support
- Issues: GitHub Issues
- Discord/Slack: [TBD]

---
**Made with ❤️ for book lovers** | Scales to **1M+ users** 🚀

