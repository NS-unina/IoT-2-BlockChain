FROM ethereum/client-go:alltools-v1.10.10

COPY ./data/ /root/
COPY ./keystore /root/.ethereum/keystore

RUN geth --nousb init /root/genesis.json

#ENTRYPOINT [ "geth" ]                                                                                                                                                                       