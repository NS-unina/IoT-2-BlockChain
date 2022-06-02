FROM ethereum/client-go:alltools-v1.10.1

COPY ./data/ /root/
COPY ./keystore /root/.ethereum/keystore

RUN geth --nousb init /root/genesis.json

RUN rm -f ~/.ethereum/geth/nodekey

