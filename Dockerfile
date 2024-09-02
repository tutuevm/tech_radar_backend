
FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tech_radar_backend
ENV PYTHONPATH=/tech_radar_backend

COPY requirements/requirements.txt ./requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

COPY . /tech_radar_backend


WORKDIR /tech_radar_backend/src

CMD ["python", "-m", "main"]