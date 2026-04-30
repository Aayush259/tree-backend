# Tree Backend

A Django-based backend for managing hierarchical tree structures. This project provides a RESTful API to interact with tree data and uses PostgreSQL for persistent storage.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10+**
- **Docker & Docker Compose** (for the database)
- **pip** (Python package manager)

## Local Setup Instructions

Follow these steps to get the project running on your local machine:

### 1. Clone the Repository
```bash
git clone <repository-url>
cd tree-backend
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the following variables. You can copy the template below:

```env
DEBUG=True
APP_URL="http://localhost:5173"
POSTGRES_DB="tree"
POSTGRES_USER="admin"
POSTGRES_PASSWORD="admin123"
```

### 5. Start the Database
The project uses PostgreSQL, which is configured via Docker Compose.
```bash
docker compose up -d
```
This will start a PostgreSQL container named `tree_db`.

### 6. Run Migrations
Apply the database migrations to set up the schema.
```bash
python manage.py migrate
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET /api/tree/**: Retrieve the full tree structure.
- **POST /api/tree/**: Add a new node or perform tree operations.

## Deployment

The project includes a GitHub Actions workflow for deployment and uses Gunicorn with WhiteNoise for serving static files in production.
