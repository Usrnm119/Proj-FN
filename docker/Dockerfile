FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /install-deps

# Final stage: set up runtime with installed deps and application code
FROM python:3.11-slim
WORKDIR /app

# Copy dependencies installed in the builder stage
COPY --from=builder /install-deps /usr/local/lib/python3.11/site-packages

# Copy the application source
COPY . .

# Expose the application port
EXPOSE 5000

# Launch the app
CMD ["python3", "app.py"]

