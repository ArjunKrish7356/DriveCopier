FROM python:3.10-slim

# Install system dependencies needed for DeepFace
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create directories for mounting external volumes
RUN mkdir -p /app/input /app/all_images /app/verified_images

# Set these directories as volumes
VOLUME ["/app/input", "/app/all_images", "/app/verified_images"]

# Run the application
CMD ["python3", "main.py"]