FROM python:3.10-slim-bookworm

RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade --requirement requirements.txt

COPY . .

CMD ["python3", "-m", "BrandrdXMusic"]
