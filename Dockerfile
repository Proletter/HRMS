FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libcairo2-dev gcc

WORKDIR /app/

COPY . .

RUN chmod +x /app/entrypoint.sh

RUN pip install -r requirements.txt

RUN /app/entrypoint.sh

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
