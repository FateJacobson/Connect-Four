FROM python:2.7

ADD connect_four.py .

ADD test.py .

RUN apt update

RUN apt-get -y install python-pip

RUN pip install coverage

CMD [ "python", "connect_four.py"]