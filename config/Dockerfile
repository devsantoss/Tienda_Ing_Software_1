FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "main.py"]
