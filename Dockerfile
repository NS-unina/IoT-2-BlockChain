FROM ethereum/client-go:alltools-v1.10.1

COPY ./data/ /root/
COPY ./keystore /root/.ethereum/keystore

RUN rm -f ~/.ethereum/geth/nodekey

RUN geth --nousb init /root/genesis.json

#ENTRYPOINT [ "geth" ]                                                                                                                                                                       
