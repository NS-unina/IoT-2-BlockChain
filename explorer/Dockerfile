FROM node:16-alpine3.14

RUN apk add --update git
RUN git clone https://github.com/zulhfreelancer/explorer.git

WORKDIR /explorer
RUN git checkout 47a567d0a63b6016816bb9e0def3039caed5dad1
CMD npm start
