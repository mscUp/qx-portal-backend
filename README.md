# QX Portal Backend API

Backend API for QX Portal - Advertising and Content Marketing Platform

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL / SQLite
- **ORM**: SQLAlchemy
- **Authentication**: JWT

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Environment

```bash
cp .env.example .env
# Edit .env with your database credentials
```

### 3. Run Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

### 4. View API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Content Management

- `GET /api/content/items` - Get all content items
- `POST /api/content/items` - Create content item
- `GET /api/content/items/{id}` - Get specific content item
- `PUT /api/content/items/{id}` - Update content item
- `DELETE /api/content/items/{id}` - Delete content item

### Banners

- `GET /api/banners` - Get all banners
- `POST /api/banners` - Create banner
- `PUT /api/banners/{id}` - Update banner
- `DELETE /api/banners/{id}` - Delete banner

### Features

- `GET /api/features` - Get all features
- `POST /api/features` - Create feature
- `PUT /api/features/{id}` - Update feature
- `DELETE /api/features/{id}` - Delete feature

## Database Setup

### Using SQLite (Default)

No setup required. Database file will be created automatically as `qx_portal.db`

### Using PostgreSQL

1. Create database:
```sql
CREATE DATABASE qx_portal;
```

2. Update `.env`:
```
DATABASE_URL=postgresql://user:password@localhost:5432/qx_portal
```

### Using Supabase (Free PostgreSQL)

1. Create project at https://supabase.com
2. Copy database URL from Settings > Database
3. Update `.env`:
```
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[REF].supabase.co:5432/postgres
```

## Deployment

### Railway (Recommended, Free)

1. Install Railway CLI: https://docs.railway.app/develop/cli
2. Login: `railway login`
3. Deploy: `railway up`

### Render (Free)

1. Connect GitHub repo
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Project Structure

```
qx-portal-backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app entry
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   └── routers/          # API routes
│       ├── content.py
│       ├── banners.py
│       └── features.py
├── uploads/              # Uploaded files
├── requirements.txt
├── .env.example
└── README.md
```

## Development

### Run with auto-reload
```bash
uvicorn app.main:app --reload --port 8000
```

### Test API
```bash
curl http://localhost:8000/health
```

## License

MIT
