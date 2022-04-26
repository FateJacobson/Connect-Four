FROM python:2.7

ADD connect_four.py .

CMD [ "python", "connect_four.py"]