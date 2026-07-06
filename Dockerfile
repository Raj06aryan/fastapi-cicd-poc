# Dockerfile -- > A recipe for building a Docker image for our FastAPI application

# step-1 : start from an official python image
FROM python:3.13-slim

# step-2 : set the working directory in the container
WORKDIR /app

# step-3 : copy the dependency list
COPY requirements.txt .

# step-4 : install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# step-5 : copy the application code
COPY . .

# step-6 : expose the application port
EXPOSE 8000

# step-7 : start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]