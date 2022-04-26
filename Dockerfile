FROM python:2.7

ADD connect_four.py .

RUN apt update

CMD [ "python", "./connect_four.py" ]