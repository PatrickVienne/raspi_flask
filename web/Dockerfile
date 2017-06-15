FROM resin/rpi-raspbian:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libffi-dev libssl-dev
RUN pip install -U pip
RUN apt-get install libmysqlclient-dev
COPY * /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80 430
ENTRYPOINT ["python"]
CMD ["app.py"]

