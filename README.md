# InitiativeTracker

D&D combat encounter tracker built with FastAPI, React, PostgreSQL and Docker.

## Run with Docker

### Requirements

- Docker
- Docker Compose

### Start

Clone the repository:

```bash
git clone https://github.com/darthrozwell/initiativetracker.git
cd initiativetracker
```

Create .env in the project root:

```
POSTGRES_DB=initiative_tracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Start all services:

```
docker compose up --build
```

Open:
```
http://localhost
```
Stop

```
docker compose down
```

To remove containers and database data:
```
docker compose down -v
```
Services
- Frontend — React + Vite + Nginx
- Backend — FastAPI + Uvicorn
- Database — PostgreSQL
