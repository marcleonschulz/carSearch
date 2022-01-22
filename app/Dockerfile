FROM python:3.11

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt --no-cache

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "main:app","--host","0.0.0.0"]