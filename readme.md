# IoT 2 BlockChain 

Il seguente progetto ha lo scopo di mostrate tutti i vantaggi che può portare l'implementazione del paradigma Web3 nel constesto dell'Internet of Thighs (IoT).
Con questa soluzione si vuole mostare come una BlockChain privata può essere utilizzata per la validazione dei dati prodotti da un numero massivo di dispositivi smart. Tale aspetto è un importante requisito funzionale richiesto dalle architetture *Zero-Trust*. Le suddette architetture sono progettate secondo il principio *“verify and never trust"* e pertanto qualsiasi sistema all'interno dell'infrastruttura informatica deve essere considerato "non fidato" e le sue azioni devono essere monitorate e verificare al fine di indentificare eventuali compromissioni. 

**Questo progetto risulta essere una Proof of Concept. La sua realizzazione ha il solo scopo di mostrare la fattibilità di implementazione dei requisiti precedentemente descritti**

## Deploy 
Per facilitare il deploy del seguente progetto l'architettura è stata realizzata attraverso l'utilizzo di container Docker. 

Il bootstrap può essere effettuato attraverso l'utilizzo del seguente comando.

```
docker-compose up -d
```

Nel caso non si abbia installato sul proprio device docker o docker-compose si consiglia di leggere la documentazione contenuta nei seguenti link.

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

---------------------------------------------------

## Architettura
In figura è riportata l'architettura del suguente progetto. 

![IoT2Blockchain-arch](/img/IoT2Blockchain-arch.png)

Per comprendere il funzionamento di ogni singolo componente mostrato all'interno di questo schema architetturale bisogna innanziotutto conoscere nel dettaglio il funzionamento di una BlockChain e in particolare di Ethereum. 


### BlockChain
La BlockChain può essere vista come un *"database pubblico e condiviso"* tra i diversi nodi che fanno parte della rete. 
Tale base di dati, come evidenziato dalla etimologia della parola *blockChain*, risulta essere composta da due elementi caratteristi:
- con il termine **blocco** (*block*) si fa riferimento ad una unità indivisibile adibita alla memorizzazione delle diverse informazioni che gli utenti della network desiderano conservare (ad es. transazioni).
- con il termine **catena** (*chain*) si vuole indicare che ogni blocco risulta essere crittograficamente collegato ad un suo blocco padre. Questo attributo garatisce che i dati contenuti all'interno di un blocco non possono variare se non modificando tutti i blocchi successivi. 

![IoT2Blockchain-arch](/img/blockchain.png)






Nella nostra rchitettura sono presenti due nodi miner e uno athoritive 
per comprendere la loro funzione si bisogna spiegare il funzionamento dell'algortimo di consenso proof-of -authority
La scelta dell'algoritmo proof-of-authority è stata determinata da alcuni requisiti applicativi e pertanto in una fase progettuale tale algoritmo di consenso potrebbe variare.

New blocks are broadcast to the nodes in the network, checked and verified, thus updating the state of the blockchain for everyone.



Le informazioni contenute in questa particolare base di dati risultano essere divise in blocchi. Infatti, con il termine *blocco* facciamo riferimento ad una unità idnvisibile cha ha lo scopo di conservare alcune delle informazioni richieste
I nodi che compongono la nostra private block chain risultano essere raggruppati all'interno del rettagolo giallo. In particolare, si può analizare la presenza di tre miner-node e di un bootstap node.


## Exposed secrice 
**EthStat**

http://localhost:3000


**RealTime Dashboard**

http://localhost:5000

**Explorer**

http://localhost:8000

