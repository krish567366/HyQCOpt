FROM python:3.9-slim
WORKDIR /app

# Install core HyQCOpt
COPY ../../core /app/core 
RUN pip install -e /app/core

# Install service dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "-m", "awslambdaric", "app.handler"]