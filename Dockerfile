FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install -vv
