FROM python:3.10.4-slim-bullseye

EXPOSE 3000

WORKDIR /app

ENV FLASK_APP app.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["bash","initdocker.sh"]