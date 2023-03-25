FROM docker.io/library/python:3.10-alpine

WORKDIR /app_name

COPY requirements.txt /app_name/
RUN pip install -r requirements.txt

COPY app_name /app_name/

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP="app_name"

WORKDIR /

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]