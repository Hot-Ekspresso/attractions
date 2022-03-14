FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./models.py /code/models.py
COPY ./populate.py /code/populate.py
COPY ./schemas.py /code/schemas.py
COPY ./database.py /code/database.py
COPY ./tourist_attractions.csv /code/tourist_attractions.csv

RUN ["python", "/code/populate.py"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
