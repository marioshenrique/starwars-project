FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3.10 python3.10-venv python3.10-dev python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /src
ENV PYTHONPATH=/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
COPY .env .
COPY src .
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]