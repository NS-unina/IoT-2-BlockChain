FROM alpine:3.16.0

COPY ./code/ /root/

WORKDIR /root
RUN apk add --update --no-cache python3 py3-pip
RUN pip install -r requirement.txt

CMD python3 publisher.py