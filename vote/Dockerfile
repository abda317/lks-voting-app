FROM python:3.9-alpine

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
