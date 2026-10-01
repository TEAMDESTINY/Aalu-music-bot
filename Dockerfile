FROM python:3.10-slim-bookworm

# ffmpeg और git एक ही RUN में install करें, और apt cache साफ करें
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/
COPY . /app/

RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# CMD को JSON array format में लिखें
CMD ["python3", "-m", "BrandrdXMusic"]
