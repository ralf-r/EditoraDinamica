FROM python:3.12.6

ENV PYTHONUNBUFFED = 1

WORKDIR  /code 

COPY rq.txt .

RUN pip install -r rq.txt

COPY . . 

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]