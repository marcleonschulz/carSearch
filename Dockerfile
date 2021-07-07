FROM python:3-slim

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt --no-cache

COPY ./app /app

WORKDIR /app

CMD ["uvicorn", "main:app","--host","0.0.0.0"]