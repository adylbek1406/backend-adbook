-- Postgres init for AdBook
-- Run on first startup via docker-compose

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Custom indexes for search (migrate will add model indexes)
CREATE INDEX IF NOT EXISTS idx_users_fulltext ON apps_accounts_user USING gin(to_tsvector('english', username || ' ' || first_name || ' ' || last_name));

-- Production settings
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET shared_preload_libraries = 'pg_trgm';
SELECT pg_reload_conf();

-- Vacuum settings
ALTER SYSTEM SET autovacuum = on;
ALTER SYSTEM SET log_min_duration_statement = 250;
SELECT pg_reload_conf();

