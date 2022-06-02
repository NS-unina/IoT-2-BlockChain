FROM node:16-alpine3.14

RUN apk add --update git
RUN npm install -g grunt
RUN git clone https://github.com/goerli/ethstats-server.git

WORKDIR /ethstats-server
RUN git checkout 0a4a93cd745e9d97a42678fbf5658fd57644570e
RUN npm install && grunt poa
CMD npm start
