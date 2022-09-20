# IoT 2 BlockChain 

Il seguente progetto ha lo scopo di mostrate tutti i vantaggi che può portare l'implementazione del paradigma Web3 nel constesto dell'Internet of Thighs (IoT). Con questa soluzione si vuole mostare come una BlockChain privata può essere utilizzata per la validazione dei dati prodotti da un numero massivo di dispositivi smart. Tale aspetto è un importante requisito funzionale richiesto dalle architetture *Zero-Trust*. Le suddette architetture sono progettate secondo il principio *“verify and never trust"* e pertanto qualsiasi sistema all'interno dell'infrastruttura informatica deve essere considerato "non fidato" e le sue azioni devono essere monitorate e verificare al fine di indentificare eventuali compromissioni. 

**Questo progetto risulta essere una Proof of Concept. La sua realizzazione ha il solo scopo di mostrare la fattibilità di implementazione dei requisiti precedentemente descritti.**

## Architettura
Per comprendere al meglio il funzionamento della soluzione proposta viene descritto di seguito il ruolo di ogni componente presente all'interno dell'ecosistema IoT2BlockChain (Fig.\ref{Infra_IoT2BlokChain}):

L'architettura proposta ha lo scopo di mostrare come Ethereum e gli Smart Contract possano essere utilizzati per garantire l’integrità, la tracciabilità e la consistenza del dato raccolto da un generico sensore IoT. Il raggiungimento di tale obiettivo è reso possibile integrando le tecnologie appena citate, con i principi architetturali dell’edge computing.

![IoT2Blockchain-arch](/img/edgeComputing.jpg)

Tale paradigma prevede che venga creata un’infrastruttura IT decentralizzata e distribuita che abbia il compito di elaborare i dati raccolti dagli smart device e successivamente registrarli su una blockchain privata. Tale approccio, oltre a ridurre notevolmente il traffico di rete, permette di offrire una soluzione maggiormente resiliente e scalabile. Infine, per verificare il corretto funzionamento dell’architettura `e stata sviluppata una web application che permette di visualizzare tutti i dati memorizzati all’interno della blockchain.

Di seguito si fornisce uno schematico dell'infrastruttura creata e una breve descrizione di ogni componente ivi presente.

- il nodo **subscriber** analizza e processa tutti i dati raccolti dai sensori e resi disponibili dai nodi publisher. Esso assume anche il compito di fare da **Proxy** verso la blockchain, effettuando tutte le operazioni necessarie per la memorizzazione dei dati all'interno della stessa;
- il **broker** è un software che consente la comunicazione asincrona e lo scambio di messaggi tra il publisher e i subscriber;
- il **miner** è un particolare nodo della blockchian che risulta essere autorizzato ad inserire nuovi blocchi all'interno della struttura dati;
- il servizio **bootnode** fornisce a tutti i miner node le informazioni necessarie per individuarsi vicendevolmente;
- il servizio **Ethstat** fornisce un'interfaccia visiva per monitorare lo stato della rete ethereum;
- il servizio **Explorer** permette di visualizzare il contenuto di ogni blocco presente all'interno della blockchain;
- il **server** espone un servizio HTTP che permette di visualizzare in tempo reale la telemetria dei dati raccolti dai nodi publisher e pubblicati all'interno della blockchain. 

![IoT2Blockchain-arch](/img/IoT2Blockchain-arch.png)

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


Al fine di poter avviare l'architettura nella maniera corretta risulta necessario aver installato i seguenti applicativi sul proprio sistema: 
\begin{itemize}
- git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    \item docker (https://docs.docker.com/engine/install/)
    \item docker-compose (https://docs.docker.com/compose/)
\end{itemize}
Inoltre, per effettuare l'installazione del software mancante si consiglia di seguire le istruzioni presenti all'interno dei link indicati nella lista.



## Exposed secrice 
**EthStat**

http://localhost:3000


**RealTime Dashboard**

http://localhost:5000

**Explorer**

http://localhost:8000

