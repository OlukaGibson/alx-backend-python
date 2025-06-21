# Use Python 3.10 base image
FROM python:3.10

# Set environment variable to prevent Python buffering issues
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire app code into the container
COPY . .

# Expose port 8000 (default for Django development server)
EXPOSE 8000

# Reminder for port mapping when running the container: docker run -p 8000:8000 messaging_app_image

# Default command to run your Django app with auto-reload
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
