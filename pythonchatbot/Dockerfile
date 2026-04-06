# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies (if requirements.txt exists)
RUN pip install --no-cache-dir -r requirements.txt

# Run your app
CMD ["python", "simple_chatbot.py"]
