FROM python:3.10.5-bullseye
COPY ./code/ /root/

WORKDIR /root
RUN pip install -r requirement.txt

CMD flask run --host=0.0.0.0