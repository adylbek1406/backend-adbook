# AdBook Бэкенд

Производственный Django REST API бэкенд для AdBook — социальной платформы для книг, заметок и рецензий (похожей на Instagram для любителей книг).

## Функции

- 🔐 **Аутентификация** — JWT с регистрацией, входом, выходом
- 📚 **Книги** — CRUD книг с обложками и рецензиями
- 📝 **Посты/Заметки** — текстовые посты с изображениями
- 💬 **Комментарии** — вложенные комментарии к книгам/постам
- ❤️ **Лайки** — универсальная система лайков
- 👥 **Подписки** — подписка/отписка от пользователей
- 📂 **Коллекции** — личные коллекции книг/постов
- 🔔 **Уведомления** — реального времени (WebSocket)
- 💭 **Чат** — личные сообщения (WebSocket)
- 📱 **Лента** — персонализированная от подписок
- 🔍 **Поиск** — полнотекстовый по пользователям/книгам

## Технологический стек

```
Backend: Django 5 + DRF + Celery + Channels
DB: PostgreSQL (GIN search, partitioning)
Cache: Redis 7
WebSocket: Django Channels
Server: Gunicorn + Nginx
DevOps: Docker Compose
```

## 📁 Структура проекта

```
adbook-backend/
├── apps/
│   ├── accounts/           # Пользователи, JWT, Profile, OTP
│   ├── books/              # Книги + рецензии
│   ├── posts/              # Посты + изображения
│   ├── comments/           # Комментарии
│   ├── likes/              # Лайки
│   ├── subscriptions/      # Подписки
│   ├── collections/        # Коллекции
│   ├── notifications/      # Уведомления
│   ├── chat/               # Чат WebSocket
│   ├── feed/               # Лента
│   └── search/             # Поиск
├── config/                 # Django настройки (dev/prod)
├── core/                   # Базовые модели/utils
├── docker-compose.yml      # Docker (Postgres+Redis+Web+Nginx)
├── Dockerfile              # Django app container
├── nginx.conf              # Production nginx
├── requirements.txt        # Все зависимости
├── manage.py
└── media/                  # User uploads
```

## 🚀 Быстрый старт

```bash
cd adbook-backend
# venv + pip install -r requirements.txt (уже сделано)
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

**Admin:** `http://127.0.0.1:8000/admin/`
**API Docs:** `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`

## 📱 API Endpoints для фронтенда

```
Auth: POST /api/v1/register/ | /login/
Books: GET/POST /api/v1/books/
Posts: GET/POST /api/v1/posts/
Profile: GET /api/v1/accounts/me/
Follow: POST /api/v1/subscriptions/{id}/follow/
Chat WS: ws://localhost:8000/ws/chat/
Notifications WS: ws://localhost:8000/ws/notifications/
```

## 🐳 Production Docker

```bash
cp .env.example .env
docker compose up --build -d
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

## ✅ Готов к деплою и фронтенду!

**Фронтенд инструкция:**
1. `npm create vite@latest frontend`
2. `axios.defaults.baseURL = 'http://localhost:8000/api/v1/'`
3. JWT auth + WebSocket (socket.io-client)
4. Swagger UI для теста endpoints

**Лицензия:** MIT
