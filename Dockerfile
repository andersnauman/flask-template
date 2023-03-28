FROM docker.io/library/python:3.10-alpine

WORKDIR /app_name

COPY requirements.txt /app_name/
RUN pip install -r requirements.txt

COPY app_name /app_name/

ENV PYTHONUNBUFFERED=1

WORKDIR /

CMD [ "waitress-serve", "--port=5000", "--call", "app_name:create_app"]