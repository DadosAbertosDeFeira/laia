FROM python:3.7.3

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN python -m pip install --upgrade pip
RUN pip install poetry==1.4.1
RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install -vv
