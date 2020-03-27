FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3.6 python3-pip


RUN mkdir /opt/savanamedapi

ENV PYTHONPATH=/opt/

COPY ./ /opt/savanamedapi/
COPY    pip.conf /root/.pip/

RUN pip3 install --upgrade pip==9.0.3 && \
    pip3.6 install -r /opt/savanamedapi/requirements.txt


VOLUME /opt/log


WORKDIR /opt/savanamedapi

CMD ["python3", "/opt/savanamedapi/launcher.py"]