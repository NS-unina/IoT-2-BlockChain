FROM ethereum/client-go:alltools-v1.10.10

COPY ./data/ /root/

RUN geth --nousb init /root/genesis.json

RUN geth --networkid 1234 --port 30303 --ipcdisable --syncmode full --http --http.addr 0.0.0.0 --http.api admin,eth,miner,net,txpool,personal,web3 --allow-insecure-unlock --http.corsdomain “*” --http.vhosts “*” --http.port 8545 --unlock 0xa273a5c973a6be46ca427d4201b8ab967c04624a --mine console --password /root/.ethereum/keystore/password.txt
