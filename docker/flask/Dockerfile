FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install paho-mqtt
CMD python app.py