# AdBook FULL ER Schema (22 Tables)

## 🗄️ **CORE ENTITIES** (Scale-Optimized w/ Indexes)

```
USERS (5 tables) ──────────────── POSTS (4 tables)
├── User (PK: id, email, phone)    ├── Post ↔ Book FK
├── Profile 1:1                    ├── PostImage (*)
├── Device (*)                     ├── PostShare (*)
├── LoginHistory (*)               └── PostLike (*)
└── OTP (*)
                           │
                           ▼
FOLLOWERS (2 tables) ───── RELATIONSHIPS ── COMMENTS (2 tables)
├── Follower (M:N)                 ├── Comment ↔ Post (*)
└── Subscription (1:N)             └── CommentLike (*)

BOOKS (2 tables)
├── Book (title, isbn, search_vector)
└── BookReview (1:N)

CHAT (4 tables)
├── ChatRoom
├── ChatRoomMember (M:N)
├── Message (*)
└── MessageRead (M:N)

NOTIFICATIONS (2 tables)
├── Notification (*)
└── NotificationPreference (1:1)

COLLECTIONS (2 tables)
├── Collection (1:N)
└── SavedItem (polymorphic Book/Post)

FEED & SEARCH (3 tables)
├── FeedCache (1:1 per type)
├── FeedInteraction (*)
└── SearchIndex
```

## 📊 **INDEXING STRATEGY** (1M Users Optimized)

```
1. **Composite FK Indexes** (80% queries): user_id + timestamp
2. **GIN Full-text** (Books/Search): 200ms queries
3. **Partial Active**: WHERE is_active AND last_seen > NOW() - INTERVAL '30 days'
4. **Covering Indexes**: SELECT count(*) FROM posts WHERE author_id=1
5. **Redis Cache Keys**:
   - user:123:feed → JSON post_ids (TTL 5m)
   - post:456:likes → SET user_ids
   
POSTGRES OPTIMIZATIONS:
- PARTITIONING: posts by date_joined (yearly)
- CONNECTION POOLING: PgBouncer (200 max)
- READ REPLICAS: 3x for feed/search
```

## 🔗 **Key Relationships**
```
Post → Author (FK User)           CASCADE
Post → Book (FK nullable)         RESTRICT
Comment → Post (FK) (*)           millions
Follower (User↔User) M:N          unique constraint
ChatMessage → Room (*)            partitioned
Notification → User (*)           unread index
```

## ⚡ **SCALABILITY METRICS**
```
Expected Load (1M users):
- Posts: 10M rows/year
- Messages: 100M rows/year  
- Queries/sec: 5k rps
- Cache Hit: 95% Redis
```

**Generated Tables**: 22 total with production indexes.

