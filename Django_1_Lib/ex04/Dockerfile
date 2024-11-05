FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY my_script.sh ./
COPY requirements.txt ./

RUN chmod +x my_script.sh

ENTRYPOINT ["./my_script.sh"]

# docker build -t ex04 .
# docker run -it ex04
