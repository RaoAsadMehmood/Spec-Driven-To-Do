# Database Schema Template

This is a placeholder for database schema specifications.

## Tables

### users
- id: UUID (primary key)
- username: VARCHAR(50) (unique, not null)
- email: VARCHAR(100) (unique, not null)
- created_at: TIMESTAMP (not null)
- updated_at: TIMESTAMP (not null)

### tasks
- id: UUID (primary key)
- user_id: UUID (foreign key to users.id)
- title: VARCHAR(200) (not null)
- description: TEXT
- status: VARCHAR(20) (not null, default: 'pending')
- created_at: TIMESTAMP (not null)
- updated_at: TIMESTAMP (not null)

## Indexes
- users.username_idx: INDEX ON users(username)
- users.email_idx: INDEX ON users(email)
- tasks.user_id_idx: INDEX ON tasks(user_id)
- tasks.status_idx: INDEX ON tasks(status)

## Constraints
- users.email_chk: CHECK email is valid format
- tasks.status_chk: CHECK status in ('pending', 'in_progress', 'completed')