# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
