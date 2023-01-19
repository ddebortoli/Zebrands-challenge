### Base
FROM ubuntu:latest
WORKDIR /usr/src/app
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt ./
RUN pwd && ls

### Config Ubuntu
RUN apt-get --assume-yes update   
RUN apt-get --assume-yes install python2-dev python3-pip curl
RUN pip install mysql-connector-python
RUN apt install default-libmysqlclient-dev -y --assume-yes
RUN pip install --no-cache-dir -r requirements.txt



### Network and Run ;)
EXPOSE 80
COPY ./src ./src
# COPY ./db.config.json ./
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:8005 --workers=3 --timeout 500 --chdir /usr/src/app/src run:app --disable-redirect-access-to-syslog"]
