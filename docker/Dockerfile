
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /install-deps

FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /install-deps /usr/local/lib/python3.11/site-packages

COPY . .


CMD ["python3", "app.py"]
```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python3", "app.py"]
