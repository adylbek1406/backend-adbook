# AdBook Backend Development TODO
Current Working Directory: /Users/adylbek/Desktop/backend_adbook

## Approved Plan Status
✅ **Phase 1: Project Skeleton** - Completed by BLACKBOXAI

**Updated Phases (User Priorities: Auth → Core Models → Follow → Feed → Chat/Notifs → Search)**
✅ **Phase 1 Steps:**
- [x] Update TODO.md (tracked here)
- [x] Create project root files: README.md, .gitignore, .env.example
- [x] Verify docker-compose.yml, Dockerfile, docker/nginx.conf
- [x] Verify config/ settings structure (base.py, dev.py, prod.py, urls.py, wsgi.py)
- [x] Verify core/ shared utils
- [x] Verify 12 apps/ directories with __init__.py
- [x] Verify requirements.txt

✅ **Phase 2 Progress: Core Models** 
- [x] accounts/models.py + apps.py + admin.py + signals
- [x] books/apps.py + admin.py 
- [x] posts/models.py + apps.py + admin.py
- [x] comments/models.py + apps.py + admin.py
- [ ] likes/models.py 
- [x] subscriptions/models.py + apps.py + admin.py
- [ ] Later: collections, notifications, chat, feed, search
- [ ] Migrations + tests

⏳ **Phase 3: Authentication System**
- [ ] Complete JWT + OTP backend + Redis blacklist
- [ ] accounts/urls.py, serializers.py (complete), services/selectors

⏳ **Phase 4: Core APIs + WebSockets** (Posts/Feed/Follow)
- [ ] All serializers/views/urls.py for priority apps
- [ ] Channels for chat/notifications

⏳ **Phase 5: Service/Selector Layers + Optimizations**

## Next Steps (Run After Approvals)
1. Review/approve created files
2. `cp .env.example .env` & edit secrets
3. `docker compose up --build`
4. `docker compose exec backend python manage.py makemigrations`
5. `docker compose exec backend python manage.py migrate`
6. `docker compose exec backend python manage.py createsuperuser`
7. Test: `curl http://localhost/api/v1/health/`

**Legend**: [x] Done | [] Pending | ⏳ Planned
