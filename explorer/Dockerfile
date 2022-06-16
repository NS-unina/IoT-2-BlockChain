FROM node:16-alpine3.14

RUN apk add --update git
RUN git clone https://github.com/zulhfreelancer/explorer.git

WORKDIR /explorer
RUN git checkout cc268475fd00fba1165b84450291850198368e11
CMD npm start
