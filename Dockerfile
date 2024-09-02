
FROM python:3.12.4-slim


WORKDIR /tech_radar_backend


COPY requirements/requirements.txt ./requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

COPY . /tech_radar_backend

ENV PYTHONPATH=/tech_radar_backend


WORKDIR /job_exchange/src

CMD ["python", "-m", "main"]