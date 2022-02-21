<div align="center">
    <img src="https://wagtail.io/static/img/wagtail.dbf60545a188.svg" alt="Bootstrap logo" width="200">
    <h1>Wagtail Starter Project</h1>
</div>

## Descrizione:

Un template che permetta di ottimizzare e automatizzare quelle che sono le operazioni comuni per l'inizio di ogni progetto Wagtail.
Inoltre migliora quello che è lo sviluppo del progetto, permettendoci di sfruttare al massimo le tecnologie quali `ES6`, `SASS`, `Boostrap4`, `Gulp (Task runner)`, `Webpack`, `Docker`.
Infine, con il metodo `CI/CD`, ci permette di introdurre l'automazione nelle diverse fasi di sviluppo del progetto, che si basa sui concetti di `Integrazione`, `Distribuzione` e `Deployment` continui.

## Installazione:

Per utilizzare questo template, segui qui sotto i dettagli per una corretta installazione. Le operazioni che affronteremo saranno sul **Server remoto**, nella nostra nuova **Repository** e in **Locale**.

#### Server remoto

1. Crea cartella di progetto
2. Crea ambiente virtuale e chiamalo `env`
3. Crea DB Postgres per la produzione

#### Repository & Locale

4. Crea una repository vuota per il tuo progetto
5. Clona in locale la "repository template" di riferimento:

```
git clone <LINK-REPO-TEMPLATE> <NOME-CARTELLA> && rm -rf ./<NOME-CARTELLA>/.git
```

6. Inizializza la repository creata:

```
git init

git branch -M master

git remote add origin <LINK-REPO-PROGETTO-CREATA>
```

7. Modifica i seguenti file come da indicazioni che trovi all'interno dei file: `.github/workflow/deploy-live.yml`, `Makefile`, `package.json`, `./src/docker-compose.yml`

8. Modifica le credenziali per il database di produzione creato nel file `../settings/production.py`

9. **Commit** e **Push** di tutta la repository **escludendo** il file `.github/workflow/deploy-live.yml`

10. (a) Aggiungi **chiave-ssh** al tuo repository in `settings/secrets` aggiungendo come parametri `HOST`, `PORT`, `USERNAME`, `SSHKEY`

11. **Commit** e **Push** del file `.github/workflow/deploy-live.yml`

12. Crea un **branch** chiamato `development` per il tuo sviluppo del progetto

## Utilizzo:

Per poter utilizzare questo template si richiede di aver installato in locale `Node`, `Docker`, `PgAdmin`.
Se non li hai installati segui le istruzioni per l'installazione:
=> [Node](https://nodejs.org/it/download/)
=> [Docker](https://docs.docker.com/get-docker/)
=> [PgAdmin](https://www.pgadmin.org/download/)

#### Quick start

- Avvia il comando `make compose-start`, che installera la nostra macchina virtuale con Docker necessaria per il "Backend"
- Avvia il comando `npm init`, che installera tutti i pacchetti necessari per il "Frontend"
- Avvia il comando `npm run dev`, per iniziare lo sviluppo

#### Frontend

Grazie a `Gulp` e `Webpack` possiamo sfruttare tutta la potenza di `Bootstrap`, `Sass` e la nuova versione di Javasript `ES6`.
Questo "toolbox" ci permette di compilare e minimizzare in soli 2 file i nostri file `.css` e `.js` del nostro progetto Wagtail.
Infine grazie a `BrowserSync` abbiamo la possibilità di fare "tunnel" tra il runserver di django e il nostro browser per un reload automatico delle nostre modifiche.

#### Backend

Grazie a `Docker` avvieremo la nostra macchina virtuale che ci permetterà di avere un'ambiente identico a quello presente sul nostro server di sviluppo.
In questo modo potremmo utilizzare come database `Postgres` per replicare il nostro database di produzione.

---

### Happy coding 🥳

---
