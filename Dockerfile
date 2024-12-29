FROM python:3.11.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose FastAPI's port
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app.hello:app", "--host", "0.0.0.0", "--port", "8000"]