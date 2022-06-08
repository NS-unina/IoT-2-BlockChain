FROM node:16-alpine3.14

RUN apk add --update git
RUN git clone https://github.com/etherparty/explorer.git

WORKDIR /explorer
RUN git checkout 9942a29cd227784df1b359c9a1dd28928167dfbb
CMD npm start
