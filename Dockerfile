FROM python:2.7

ADD connect_four.py .

ADD test.py .

ADD run_container.py .

RUN apt update

RUN apt-get -y install python-pip

RUN pip install coverage

CMD [ "python", "run_container.py"]