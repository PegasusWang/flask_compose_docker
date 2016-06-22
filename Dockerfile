FROM python:2.7.11
ADD . /flask_compose
WORKDIR /flask_compose
RUN pip install -r requirements.txt
