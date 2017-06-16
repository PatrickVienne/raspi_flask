FROM resin/rpi-raspbian:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libffi-dev libssl-dev
RUN pip install -U pip
RUN apt-get install libmysqlclient-dev
COPY * /emailapp/
WORKDIR /emailapp
EXPOSE 25
ENTRYPOINT ["python"]
CMD ["start_server.py"]

