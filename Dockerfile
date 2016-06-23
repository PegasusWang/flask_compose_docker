FROM python:2.7.11
ADD . /flask_compose
WORKDIR /flask_compose
EXPOSE 5000
RUN pip install -r requirements.txt
