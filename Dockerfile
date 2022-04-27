FROM python:3.8

ARG APP_NAME=python_project_setup
ARG APP_PATH=/opt/${APP_NAME}

ENV POETRY_HOME="/opt/poetry"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH=${POETRY_HOME}/bin:${PATH}

WORKDIR ${APP_PATH}

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . ${APP_PATH}

RUN alembic revision --autogenerate -m "create models"
RUN alembic upgrade heads

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
