# Fitness AI Service

FastAPI microservice responsible for generating AI-based training and nutrition plans for the fitness application.

The service is independent from the main Django backend and does not access the database directly. The backend sends the required user and application data, and the AI service returns structured generated plans.

## Features

* Training plan generation
* Nutrition plan generation
* OpenAI and Gemini support
* Provider selection per request
* Structured Pydantic responses
* No direct database dependency

## Tech Stack

* Python
* FastAPI
* OpenAI API
* Google Gemini API
* Docker
* Docker compose

## Architecture

```text
Frontend
   |
   v
Django Backend
   |
   v
FastAPI AI Service
   |
   +-- OpenAI
   |
   +-- Gemini
```

Django is responsible for authentication, persistence, business logic, and background tasks.

The AI service is responsible only for generating and validating AI output.

## Training Plan Generation

The backend sends user information together with the exercises available in the application.

Example request data:

```json
{
  "age": 25,
  "weight_kg": 90,
  "height_cm": 180,
  "goal_weight": 85,
  "experience_level": "intermediate",
  "days_per_week": 4,
  "available_exercises": [
    {
      "id": 1,
      "name": "Bench Press",
      "description": "Barbell horizontal pressing exercise"
    }
  ],
  "notes": ""
}
```

Generated exercises reference existing exercises by ID:

```json
{
  "exercise_id": 1,
  "sets": 4,
  "reps": 8
}
```

Training plans always contain:

```text
mon
tue
wed
thu
fri
sat
sun
```

Rest days are returned as `null`.

## AI Providers

The service currently supports:

* OpenAI
* Gemini

Providers share the same request and response models, allowing the application to switch providers without changing the API contract.

## Configuration

Create a `.env` file containing the required API credentials.

```env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
SERVICE_KEY=... (Used to authenticate requests from the main backend.)
```

## Running Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it and install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Run the service:

```bash
uvicorn main:app --reload --port 8001
```

## Running with Docker

Before initial startup create a network "fitness-tracker-network". This network must exist before starting the service. Compose will not create it automatically:

```bash
docker network create fitness-tracker-network
```

Build and start the service:

```bash
docker compose up --build
```

Start it without rebuilding:

```bash
docker compose up
```

Run it in the background:

```bash
docker compose up -d
```

Stop the service:

```bash
docker compose down
```

Once running, FastAPI documentation is available at: http://127.0.0.1:8001

```text
/docs
```

The service is exposed locally at:

## Project Structure

```text
.
├── routers/
│   └── api/
│       ├── trainingplan.py
│       └── nutritionplan.py
├── services/
│   └── providers/
├── settings/
├── models/
└── main.py
```

## Related Components

The complete application consists of:

* React frontend
* Django REST Framework backend
* PostgreSQL
* Celery
* Redis
* FastAPI AI service
