FROM python:3.8-slim-buster

# setting working directory

WORKDIR /usr/src/app

#environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
