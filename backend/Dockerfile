FROM python:3.12-slim

WORKDIR /app

# Install system deps needed for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies (no venv inside Docker)
RUN poetry config virtualenvs.create false \
    && poetry add psycopg2-binary \
    && poetry install --no-root --without dev

# Copy app source
COPY simpsonapi_playground/ ./simpsonapi_playground/

CMD ["uvicorn", "simpsonapi_playground.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
