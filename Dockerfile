FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /simplemooc
WORKDIR /simplemooc
ADD requirements.txt /simplemooc/
RUN pip install -r requirements.txt
ADD . /simplemooc/
