FROM python:3.8.12

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN python -m pip install --upgrade pip
RUN pip install poetry==1.1.15
RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install -vv
