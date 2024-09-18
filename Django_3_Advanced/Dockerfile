FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

WORKDIR /d07

COPY ./requirements.txt /requirements.txt

# Install dependencies including gettext
RUN apk add --update --no-cache \
    libffi-dev \
    build-base \
    postgresql-dev \
    postgresql-client \
    gettext \
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install -r /requirements.txt

COPY ./d07 /d07

ENV PATH="/py/bin:$PATH"

EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
