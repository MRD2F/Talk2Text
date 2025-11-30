# -------------------------------------------------------
# 1. Base image
# -------------------------------------------------------
FROM python:3.12-slim AS base

# Prevent Python from writing .pyc files and using stdout buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#additionally run export UV_HTTP_TIMEOUT=120 on local shell
ENV UV_HTTP_TIMEOUT=300
ENV PYTHONPATH="/app/src"



# -------------------------------------------------------
# 2. Install system dependencies
# -------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------------------------------
# 3. Install uv (fast Python package manager)
# -------------------------------------------------------
RUN pip install --no-cache-dir uv

# -------------------------------------------------------
# 4. Copy project metadata first (layer caching)
# -------------------------------------------------------
WORKDIR /app
COPY pyproject.toml uv.lock ./

# -------------------------------------------------------
# 5. Install dependencies using uv
# -------------------------------------------------------
RUN uv sync 
#--no-dev

# -------------------------------------------------------
# 6. Copy the actual application
# -------------------------------------------------------
COPY src/ ./src/

# -------------------------------------------------------
# 7. Expose API port and run app
# -------------------------------------------------------
EXPOSE 8000

# For Flask:
# CMD ["uv", "run", "src/myproject/app.py"]

# For FastAPI (example):
# CMD ["uv", "run", "fastapi", "run", "src/myproject/app.py"]

# More generic entrypoint:
#CMD ["uv", "run", "src/myproject/app.py"]
#CMD ["uv", "run", "src/app/convertor/service/transcription.py"]

#FROM src/app folder uv run flask --app main run
#CMD ["uv", "run", "flask", "--app", "main", "run"] 

#CORRECT from root directory
CMD ["uv", "run", "flask", "--app", "src.app.main", "run"] 