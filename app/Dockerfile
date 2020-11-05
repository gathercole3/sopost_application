FROM python:3.9.0
MAINTAINER Jacob Gathercole

RUN pip3 -q install gunicorn==19.9.0 eventlet

COPY / /opt/

RUN pip3 install -q -r /opt/requirements.txt

EXPOSE 8000

WORKDIR /opt

CMD ["/usr/local/bin/gunicorn", "-k", "eventlet", "--pythonpath", "/opt", "--access-logfile", "-", "manage:manager.app", "--reload", "-b", "0.0.0.0:8000"]
