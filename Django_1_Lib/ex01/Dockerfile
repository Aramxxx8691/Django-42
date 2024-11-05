FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y git

COPY . .

RUN pip install --upgrade pip

RUN chmod +x my_script.sh

ENTRYPOINT ["./my_script.sh"]

# Run the Project
# docker build -t ex01 .
# docker run -it ex01
# docker run -it --entrypoint bash ex01