FROM python:3.10.5-bullseye
COPY ./code/ /root/

WORKDIR /root
RUN pip install -r requirement.txt
RUN python -c "from solcx import install_solc; install_solc('v0.6.6')"

#CMD python3 publisher.py