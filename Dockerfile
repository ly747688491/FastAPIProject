FROM    python:3.10
EXPOSE 8001/tcp

RUN mkdir -p /root/.pip/ &&\
    mkdir -p /ikglobal/logs

WORKDIR /app

COPY . /app
COPY ./pip.conf /root/.pip/

RUN pip install gunicorn && pip install --no-cache-dir -r requirements.txt