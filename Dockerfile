FROM python:3.10.4-slim-bullseye

EXPOSE 5000

WORKDIR /app

ENV FLASK_APP app.py

COPY . .

CMD ["python3","initdb.py"]