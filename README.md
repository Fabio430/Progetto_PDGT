- Nome: Fabio, cognome: Giannoccoli, matricola: 279044
- Titolo del progetto: Movies API
- Breve relazione:
## 1. Descrizione del servizio implementato e del suo scopo
Il progetto consiste in un servizio web chiamato Movies API, progettato per gestire e fornire informazioni su una libreria virtuale di film.

Gli utenti possono registrarsi, autenticarsi e compiere varie operazioni, nello specifico:
1. **Aggiungere un nuovo film**.
2. **Aggiungere più film contemporaneamente (limite impostato a 200).**
3. Eliminare un film specifico tramite Id.
4. Eliminare tutti i film presenti nella libreria.
5. Modificare un film tramite l'inserimento dell'Id specifico; nel caso di Id non presente, aggiunta del nuovo film all'interno della libreria.
6. Cercare tramite Id uno specifico film.
7. Richiedere l'intera libreria di film.
8. Cercare uno specifico film tramite titolo.
9. Cercare tutti i film di un determinato genere presenti nella libreria.
10. Cercare tutti i film di uno specifico regista.
11. Cercare tutti i film di uno specifico anno.
12. Cercare tutti i film con una specifica lingua.
13. Ordinare la libreria di film in ordine crescente o decrescente secondo la durata del film.
14. Ordinare la libreria di film in ordine crescente o decrescente secondo l'Id di ogni film.
15. Ordinare la libreria di film in ordine crescente o decrescente secondo il titolo del film.
16. Ordinare la libreria di film in ordine crescente o decrescente secondo l'anno del film.
17. Ordinare la libreria di film in ordine crescente o decrescente secondo il voto del film.
18. Cercare tutti i film di una specifica decade.

Inoltre è ovviamente possibile fare il logout ed è presente una richiesta per ottenere un access token non fresh utilizzando il refresh token ottenuto al momento del login.

Lo scopo del servizio è quello di permettere l'accesso e la gestione di una libreria virtuale di film in modo sicuro e strutturato.

# 2. Descrizione di architettura e scelte implementative (componenti software, comunicazione tra componenti, tecnologie adottate, librerie, scelte implementative di rilievo, etc.)
Il servizio è stato sviluppato utilizzando Flask, un microframework per Python. L'architettura del progetto segue un modello client-server classico, dove Flask gestisce il backend e fornisce un'API RESTful.

Componenti software principali
- Flask: utilizzato per gestire le richieste HTTP, definire i route e gestire la logica dell'applicazione.
- Flask-smorest: estensione Flask utilizzata per la gestione dei blueprint. Utilizza inoltre abort per le risposte di errore. Inoltre utilizza marshmallow per definire gli schema, per la validazione e per la serializzazione(dati in uscita) e deserializzazione(dati in entrata) dei dati. Marshmallow usa gli schemi per validare automaticamente i dati e convertire oggetti Python in JSON.
- SQLAlchemy: ORM(Object-Relational Mapping) utilizzato per interagire con il database, permette di mappare classi in Python in tabelle e colonne di database, e converte oggetti Python di quelle classi in righe specifiche. Quindi permette di rendere il codice più pulito, semplice e corto.
- Flask-JWT-Extended: estensione utilizzata per implementare l'autenticazione basata su token JWT, garantendo la sicurezza delle comunicazioni tra client e server.

Comunicazione tra componenti
- La comunicazione tra i vari componenti dell'applicazione avviene tramite HTTP. Il client invia richieste HTTP al server Flask, che processa queste richieste, interagisce con il database PostgreSQL tramite SQLAlchemy, e restituisce una risposta al client. Le API seguono lo stile RESTful, il che facilita l'integrazione con diversi tipi di client, come applicazioni web, mobile, o altri servizi.

Tecnologie adottate
- Docker: utilizzato per containerizzare l'applicazione, assicurando che possa essere eseguita in ambienti diversi senza problemi di compatibilità.
- Render: piattaforma cloud utilizzata sia per l'hosting del database PostgreSQL che per il deployment dell'applicazione. Render fornisce integrazione continua, scalabilità automatica e un ambiente di produzione sicuro.
- Insomnia: utilizzato per testare le funzionalità dell'API

Librerie e moduli rilevanti
- Flask-Migrate: utilizzato per gestire le migrazioni del database, permettendo di aggiornare lo schema del database in modo sicuro e senza perdita di dati.
- Dotenv: utilizzato per caricare le variabili d'ambiente dal file '.env', separando cosi le configurazioni sensibili dal codice sorgente. In particolare nel file '.env' sono presenti l'URL del database e la secret key di JWT.
- Passlib: utilizzato per fare l'hashing della password.
- gunicorn: utilizzato in fase di deployment per le sue prestazioni, superiori a quelle di Flask.
- psycopg2: utilizzato come adattatore di database per PostgreSQL per Python.

Scelte implementative di rilievo
- Database: se non viene passato un valore per il database da app.py e non è presente un valore in .env (in questo caso è presente l'URL del database PostgreSQL su Render), il valore di default è un file SQLite locale.
- Blueprints: struttura modulare per l'organizzazione delle API, con blueprint separati per le risorse movies e users.
- Autenticazione: basata su JWT, con configurazioni per access token e refresh token.

Ulteriori informazioni
- Il file blocklist.py viene utilizzato per fare lo store degli access token e dei refresh token non più validi. Il file refresh_token_store.py invece viene utilizzato per fare lo store momentaneo del refresh token. Sono stati utilizzati dei file locali per semplicità ma probabilmente questa non è la scelta migliore né la più sicura.

# 3. Riferimento a eventuali dati o servizi esterni sfruttati
Il progetto utilizza un database PostgreSQL ospitato su Render. Il database è accessibile tramite un URL specificato nel file .env e viene utilizzato per memorizzare i dati relativi agli utenti e ai film. Inoltre, il deployment del servizio è stato effettuato su Render, una piattaforma che facilita il deploy di applicazioni web con integrazione continua e scalabilità automatica.

# 4. Documentazione dell’API implementata (URL, dettagli delle richieste HTTP supportate, formato e codifica dei dati in input ed output, etc.)

URL web service: https://progetto-pdgt.onrender.com

1. Endpoint: Registrazione Utente
    - URL: '/register'
    - Metodo HTTP: POST
    - Descrizione: Permette la registrazione di un nuovo utente.
    - Richiesta:
        - Headers:
            - Content-Type: application/json
        - Corpo:
        {
            "username": "string",
            "password": "string"
        }
    - Risposte:
        - Status Code: 201 Created
            - Corpo:
            {
                "message": "User created successfully."
            }
        - Status Code: 409 Conflict
            - Corpo:
            {
                "message": "A user with that username already exists."
            }
2. Endpoint: Login Utente
    - URL: '/login'
    - Metodo HTTP: POST
    - Descrizione: Permette a un utente registrato di effettuare il login e ottenere un token JWT.
    - Richiesta:
        - Headers:
            - Content-Type: application/json
        - Corpo:
        {
            "username": "string",
            "password": "string"
        }
    - Risposte:
        - Status Code: 200 OK
            - Corpo:
            {
                "access_token": "string",
                "refresh_token": "string"
            }
        - Status Code: 401 Unauthorized
            - Corpo:
            {
                "message": "Invalid credentials."
            }
        - Content-Type: application/json

3. Endpoint: Logout Utente
    - URL: '/logout'
    - Metodo HTTP: POST
    - Descrizione: Invalida il token JWT dell'utente corrente e disconnette l'utente.
    - Richiesta:
        - Headers:
            - Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>
    - Risposte:
        - Status Code: 200 OK
            - Corpo:
            {
                "message": "Successfully logged out."
            }
        - Status Code: 401 Unauthorized
            - Corpo:
            {
                "message": "Missing or invalid token."
            }
        - Content-Type: application/json

4. Endpoint: Token di accesso not fresh
    - URL: '/refresh'
    - Metodo HTTP: POST
    - Descrizione: Ottiene un nuovo token di accesso not fresh utilizzando un refresh token valido.
    - Richiesta:
        - Headers:
            - Authorization: Bearer <JWT_REFRESH_TOKEN>
    - Risposte:
        - Status Code: 200 OK
            - Corpo:
            {
                "access_token": "string"
            }
        - Status Code: 401 Unauthorized
            - Corpo:
            {
                "message": "Missing or invalid refresh token."
            }
        - Content-Type: application/json

1. Endpoint: Recupero Film per Decennio
    - URL: `/movie/decade/<string:decade>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera un elenco di film filtrati per decennio.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `decade` (string, ad esempio `1990s`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

2. Endpoint: Ordinamento Film per Valutazione
    - URL: `/movie/rating/sorting/<string:sort_direction>`
    - Metodo HTTP: `GET`
    - Descrizione: Ordina i film in base alla valutazione.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `sort_direction` (string, `asc` o `desc`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

3. Endpoint: Ordinamento Film per Anno
    - URL: `/movie/year/sorting/<string:sort_direction>`
    - Metodo HTTP: `GET`
    - Descrizione: Ordina i film in base all'anno di uscita.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `sort_direction` (string, `asc` o `desc`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

4. Endpoint: Ordinamento Film per Titolo
    - URL: `/movie/title/sorting/<string:sort_direction>`
    - Metodo HTTP: `GET`
    - Descrizione: Ordina i film in base al titolo.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `sort_direction` (string, `asc` o `desc`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

5. Endpoint: Ordinamento Film per ID
    - URL: `/movie/id/sorting/<string:sort_direction>`
    - Metodo HTTP: `GET`
    - Descrizione: Ordina i film in base all'ID.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `sort_direction` (string, `asc` o `desc`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

6. Endpoint: Ordinamento Film per Durata
    - URL: `/movie/runtime/sorting/<string:sort_direction>`
    - Metodo HTTP: `GET`
    - Descrizione: Ordina i film in base alla durata.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `sort_direction` (string, `asc` o `desc`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

7. Endpoint: Recupero Film per Lingua Originale
    - URL: `/movie/original_language/<string:original_language>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera i film per la lingua originale specificata.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `original_language` (string, ad esempio `english`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json
     

8. Endpoint: Recupero Film per Anno
    - URL: `/movie/year/<string:year>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera i film per l'anno specificato.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `year` (string, ad esempio `2011`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

9. Endpoint: Recupero Film per Regista
    - URL: `/movie/director/<string:director>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera i film per il regista specificato.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `director` (string, ad esempio `David Cronenberg`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

10. Endpoint: Recupero Film per Titolo
    - URL: `/movie/title/<string:title>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera i film per il titolo specificato.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `title` (string, ad esempio `Taxi driver`)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

11. Endpoint: Recupero Film per Genere
    - URL: `/movie/genre/<string:genre>`
    - Metodo HTTP: `GET`
    - Descrizione: Recupera i film per il genere specificato.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
        - Parametri URL: `genre` (string, ad esempio `crime`, `crime, drama`, ecc.)
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

12. Endpoint: Recupero, Eliminazione o Aggiornamento Film per ID
    - URL: `/movie/<string:movie_id>`
    - Metodo HTTP: GET
    - Descrizione: Recupera un film per ID.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

    - URL: `/movie/<string:movie_id>`
    - Metodo HTTP: DELETE
    - Descrizione: Elimina un film per ID.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>`
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

    - URL: `/movie/<string:movie_id>`
    - Metodo HTTP: PUT
    - Descrizione: Aggiorna un film per ID.
    - Richiesta:
        - Headers:
            - `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>`
            - Content-Type: application/json
        - Corpo:
            - esempio:
                {
                    "director": "David Cronenberg",
                    "genres": "Horror, Science-fiction",
                    "original_language": "English",
                    "runtime": "89 mins",
                    "title": "Videodrome",
                    "year": 1983,
                    "rating": "5/5"
		        }
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `201 Created`
        - Status Code: `409 Conflict`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

13. Endpoint: Aggiunta di un Nuovo Film
    - URL: `/addmovie`
    - Metodo HTTP: `POST`
    - Descrizione: Aggiunge un nuovo film.
    - Richiesta:
        - Headers:
            - `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>`
            - Content-Type: application/json
        - Corpo:
            - esempio:
		        {
                    "director": "David Lynch",
                    "genres": "Mystery, Thriller",
                    "original_language": "English",
                    "runtime": "134 mins",
                    "title": "Lost Highway",
                    "year": 1997,
                    "rating": "5/5"
		        }
    - Risposte:
        - Status Code: `201 Created`
        - Status Code: `409 Conflict`
        - Status Code: `400 Bad Request`
        - Status Code: `500 Internal Server Error`
        - Content-Type: application/json

14. Endpoint: Gestione della Lista dei Film
    - URL: `/movielist`
    - Metodo HTTP: GET
    - Descrizione: Recupera tutti i film.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>` oppure  `Authorization: Bearer <JWT_NOT_FRESH_ACCESS_TOKEN>`
    - Risposte:
        - Status Code: `200 OK`
        - Content-Type: application/json

    - URL: `/movielist`
    - Metodo HTTP: DELETE
    - Descrizione: Elimina tutti i film.
    - Richiesta:
        - Headers: `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>`
    - Risposte:
        - Status Code: `200 OK`
        - Status Code: `404 Not Found`
        - Content-Type: application/json

    - URL: `/movielist`
    - Metodo HTTP: POST
    - Descrizione: Aggiunge una lista di film.
    - Richiesta:
        - Headers: 
            - `Authorization: Bearer <JWT_FRESH_ACCESS_TOKEN>`
            - Content-Type: application/json
        - Corpo:
            - Esempio:
                [
                    {
                        "director": "Federico Fellini",
                        "genres": "Drama, comedy",
                        "original_language": "Italian",
                        "runtime": "176 mins",
                        "title": "La dolce vita",
                        "year": 1960,
                        "rating": "5/5"
                    },
                    {
                        "director": "Stanley Kubrick",
                        "genres": "Science-Fiction, Drama, Adventure",
                        "original_language": "English",
                        "runtime": "149 mins",
                        "title": "2001: A Space Odyssey",
                        "year": 1968,
                        "rating": "5/5"
                    },
                    ...
                ]
    - Risposte:
        - Status Code: `201 Created`
        - Status Code: `207 Multi-Status`
        - Status Code: `400 Bad Request`
        - Content-Type: application/json

# 5. Descrizione delle modalità della messa online del servizio
Il servizio è stato distribuito utilizzando **Render**, una piattaforma di hosting cloud che semplifica il deployment di applicazioni web e database. Il processo di messa online ha incluso i seguenti passaggi:

1. **Configurazione del Database**:
   - Il database PostgreSQL è stato configurato su Render e accessibile tramite un URL specificato nel file `.env`. Questo URL consente al servizio di interagire con il database per operazioni di lettura e scrittura.

2. **Deployment dell'Applicazione**:
   - Il deployment dell'applicazione su Render è stato fatto utilizzando il `Dockerfile` presente nel progetto. Render rileva automaticamente il file Docker e costruisce l'immagine necessaria per eseguire il servizio.
   - Le variabili d'ambiente, tra cui `DATABASE_URL` e `JWT_SECRET_KEY`, sono state configurate su Render per garantire la sicurezza e il corretto funzionamento del servizio.

3. **Integrazione Continua**:
   - Render supporta l'integrazione continua (CI), permettendo il deploy automatico delle modifiche apportate al repository. Questo assicura che ogni aggiornamento venga applicato senza interruzioni del servizio.

4. **Scalabilità e Monitoraggio**:
   - La piattaforma gestisce automaticamente la scalabilità delle risorse in base al traffico e al carico. Render fornisce anche strumenti di monitoraggio per tenere sotto controllo le prestazioni dell'applicazione e del database.

Questa configurazione permette al servizio di rimanere online, sicuro, e in grado di gestire un numero variabile di richieste, con la possibilità di scalare automaticamente secondo le esigenze.

**Piccola nota riguardante i piani utilizzati su Render**:
sono stati utilizzati piani free sia per il deployment del web service sia per la configurazione del database. Per quanto riguarda il deployment questo comporta che in caso di inattività avviene uno spin down del servizio, il che significa che la richiesta successiva impiegherà diversi secondi per essere eseguita o potrebbe non andare a buon fine, dopo di che il servizio si riattiverà.
Per quanto riguarda il database invece il piano free comporta la cancellazione dello stesso dopo 30 giorni se non si passa ad un piano a pagamento.

# 6. Esempio descrittivo di utilizzo del servizio Web (sequenza di richieste/risposte HTTP di esempio, descrizione dei dati attesi/ottenuti)

### Esempio 1: Registrazione di un Nuovo Utente

1. **Richiesta**: Registrazione di un nuovo utente
   - **Metodo HTTP**: `POST`
   - **URL**: `/register`
   - **Headers**: 
     ```
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "username": "new_user",
       "password": "secure_password"
     }
     ```
2. **Risposta**:
   - **Status Code**: `201 Created`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "User created successfully."
     }
     ```

### Esempio 2: Login di un Utente

1. **Richiesta**: Autenticazione di un utente esistente
   - **Metodo HTTP**: `POST`
   - **URL**: `/login`
   - **Headers**:
     ```
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "username": "new_user",
       "password": "secure_password"
     }
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     {
       "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
       "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
     }
     ```

### Esempio 3: Logout di un Utente

1. **Richiesta**: Logout di un utente autenticato
   - **Metodo HTTP**: `POST`
   - **URL**: `/logout`
   - **Headers**:
     ```
     Authorization: Bearer <JWT_ACCESS_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Successfully logged out"
     }
     ```

### Esempio 4: Aggiornamento del Token di Accesso

1. **Richiesta**: Ottenere un nuovo token di accesso utilizzando un refresh token
   - **Metodo HTTP**: `POST`
   - **URL**: `/refresh`
   - **Headers**:
     ```
     Authorization: Bearer <JWT_REFRESH_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     {
       "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
     }
     ```

### Descrizione dei Dati Attesi/Ottenuti

1. **Registrazione Utente**:
   - **Dati Attesi**: Username e password forniti come input JSON.
   - **Dati Ottenuti**: Messaggio di conferma che l'utente è stato creato con successo.

2. **Login Utente**:
   - **Dati Attesi**: Username e password validi come input JSON.
   - **Dati Ottenuti**: Due token JWT (access token e refresh token) in caso di successo.

3. **Logout Utente**:
   - **Dati Attesi**: Un token di accesso valido per autenticare la richiesta.
   - **Dati Ottenuti**: Messaggio di conferma che l'utente è stato disconnesso.

4. **Aggiornamento del Token**:
   - **Dati Attesi**: Un refresh token valido per autenticare la richiesta.
   - **Dati Ottenuti**: Un nuovo token di accesso JWT.

Questi esempi descrivono situazioni in cui le richieste non hanno successo, spiegando i motivi degli errori e mostrando i messaggi di risposta che l'API fornisce agli utenti.

### Esempio 1: Registrazione di un Utente con Username Duplicato

1. **Richiesta**: Tentativo di registrare un nuovo utente con un username già esistente
   - **Metodo HTTP**: `POST`
   - **URL**: `/register`
   - **Headers**: 
     ```
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "username": "existing_user",
       "password": "another_password"
     }
     ```
2. **Risposta**:
   - **Status Code**: `409 Conflict`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "A user with that username already exists."
     }
     ```

### Esempio 2: Login con Credenziali Non Valide

1. **Richiesta**: Tentativo di login con credenziali errate
   - **Metodo HTTP**: `POST`
   - **URL**: `/login`
   - **Headers**:
     ```
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "username": "new_user",
       "password": "wrong_password"
     }
     ```
2. **Risposta**:
   - **Status Code**: `401 Unauthorized`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Invalid credentials."
     }
     ```

### Esempio 3: Logout Senza Token Valido

1. **Richiesta**: Tentativo di logout senza fornire un token JWT valido
   - **Metodo HTTP**: `POST`
   - **URL**: `/logout`
   - **Headers**:
     ```
     Authorization: Bearer <INVALID_JWT_ACCESS_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `401 Unauthorized`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Missing or invalid token."
     }
     ```

### Esempio 4: Aggiornamento del Token con Refresh Token Non Valido

1. **Richiesta**: Tentativo di ottenere un nuovo access token con un refresh token non valido o scaduto
   - **Metodo HTTP**: `POST`
   - **URL**: `/refresh`
   - **Headers**:
     ```
     Authorization: Bearer <INVALID_JWT_REFRESH_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `401 Unauthorized`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Missing or invalid refresh token."
     }
     ```

### Descrizione dei Dati Attesi/Ottenuti in Caso di Errore

1. **Registrazione Utente con Username Duplicato**:
   - **Dati Attesi**: Username che esiste già nel database.
   - **Dati Ottenuti**: Messaggio di errore che indica che l'utente esiste già.

2. **Login con Credenziali Non Valide**:
   - **Dati Attesi**: Credenziali non valide (username o password errati).
   - **Dati Ottenuti**: Messaggio di errore che indica credenziali non valide.

3. **Logout Senza Token Valido**:
   - **Dati Attesi**: Token JWT mancante o non valido.
   - **Dati Ottenuti**: Messaggio di errore che indica la mancanza o l'invalidità del token.

4. **Aggiornamento del Token con Refresh Token Non Valido**:
   - **Dati Attesi**: Refresh token mancante, scaduto, o non valido.
   - **Dati Ottenuti**: Messaggio di errore che indica la mancanza o l'invalidità del refresh token.

Questi esempi coprono diversi scenari di utilizzo del servizio Web per la gestione dei film, mostrando come interagire con l'API e i dati attesi e ottenuti in ciascun caso.

### Esempio 1: Recupero Film per Decennio

1. **Richiesta**: Recuperare i film di un decennio specifico
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/decade/1990s`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     [
       {
         "id": 1,
         "title": "Pulp Fiction",
         "director": "Quentin Tarantino",
         "year": 1994,
         "genres": "Crime, Drama",
         "runtime": "154 min",
         "original_language": "English",
         "rating": "8.9"
       },
       {
         "id": 2,
         "title": "The Matrix",
         "director": "Lana Wachowski, Lilly Wachowski",
         "year": 1999,
         "genres": "Action, Sci-Fi",
         "runtime": "136 min",
         "original_language": "English",
         "rating": "8.7"
       }
     ]
     ```

### Esempio 2: Ordinamento Film per Valutazione

1. **Richiesta**: Ordinare i film in base alla valutazione in ordine decrescente
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/rating/sorting/desc`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     [
       {
         "id": 3,
         "title": "The Godfather",
         "director": "Francis Ford Coppola",
         "year": 1972,
         "genres": "Crime, Drama",
         "runtime": "175 min",
         "original_language": "English",
         "rating": "9.2"
       },
       {
         "id": 4,
         "title": "The Dark Knight",
         "director": "Christopher Nolan",
         "year": 2008,
         "genres": "Action, Crime, Drama",
         "runtime": "152 min",
         "original_language": "English",
         "rating": "9.0"
       }
     ]
     ```

### Esempio 3: Recupero Film per Genere

1. **Richiesta**: Recuperare tutti i film del genere "Sci-Fi"
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/genre/Sci-Fi`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     [
       {
         "id": 5,
         "title": "Interstellar",
         "director": "Christopher Nolan",
         "year": 2014,
         "genres": "Adventure, Drama, Sci-Fi",
         "runtime": "169 min",
         "original_language": "English",
         "rating": "8.6"
       },
       {
         "id": 6,
         "title": "Blade Runner 2049",
         "director": "Denis Villeneuve",
         "year": 2017,
         "genres": "Action, Drama, Mystery, Sci-Fi",
         "runtime": "164 min",
         "original_language": "English",
         "rating": "8.0"
       }
     ]
     ```

### Esempio 4: Aggiunta di un Nuovo Film

1. **Richiesta**: Aggiungere un nuovo film al database
   - **Metodo HTTP**: `POST`
   - **URL**: `/addmovie`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genres": "Action, Sci-Fi, Thriller",
       "runtime": "148 min",
       "original_language": "English",
       "rating": "8.8"
     }
     ```
2. **Risposta**:
   - **Status Code**: `201 Created`
   - **Corpo della Risposta**:
     ```json
     {
       "id": 7,
       "title": "Inception",
       "director": "Christopher Nolan",
       "year": 2010,
       "genres": "Action, Sci-Fi, Thriller",
       "runtime": "148 min",
       "original_language": "English",
       "rating": "8.8"
     }
     ```

### Esempio 5: Eliminazione di un Film per ID

1. **Richiesta**: Eliminare un film specifico per ID
   - **Metodo HTTP**: `DELETE`
   - **URL**: `/movie/7`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `200 OK`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Movie deleted"
     }
     ```

### Descrizione dei Dati Attesi/Ottenuti

1. **Recupero Film per Decennio**:
   - **Dati Attesi**: Parametro del decennio come parte dell'URL.
   - **Dati Ottenuti**: Lista di film usciti nel decennio specificato.

2. **Ordinamento Film per Valutazione**:
   - **Dati Attesi**: Parametro di ordinamento (`asc` o `desc`) come parte dell'URL.
   - **Dati Ottenuti**: Lista di film ordinati per valutazione.

3. **Recupero Film per Genere**:
   - **Dati Attesi**: Parametro del genere come parte dell'URL.
   - **Dati Ottenuti**: Lista di film del genere specificato.

4. **Aggiunta di un Nuovo Film**:
   - **Dati Attesi**: Informazioni dettagliate del film nel corpo della richiesta.
   - **Dati Ottenuti**: I dati del film appena creato.

5. **Eliminazione di un Film per ID**:
   - **Dati Attesi**: ID del film come parte dell'URL.
   - **Dati Ottenuti**: Messaggio di conferma dell'eliminazione del film.


Questi esempi descrivono situazioni in cui le richieste non hanno successo, spiegando i motivi degli errori e mostrando i messaggi di risposta che l'API fornisce agli utenti.

### Esempio 1: Recupero Film per Decennio con Formato Errato

1. **Richiesta**: Tentativo di recuperare film per un decennio con formato non valido
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/decade/19905`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `400 Bad Request`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Invalid decade format"
     }
     ```

### Esempio 2: Ordinamento Film con Direzione Errata

1. **Richiesta**: Tentativo di ordinare i film con una direzione di ordinamento non valida
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/rating/sorting/invalid_direction`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `400 Bad Request`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Error, invalid sort direction. Use 'asc' or 'desc'."
     }
     ```

### Esempio 3: Recupero Film per Genere Non Esistente

1. **Richiesta**: Tentativo di recuperare film per un genere non esistente nel database
   - **Metodo HTTP**: `GET`
   - **URL**: `/movie/genre/UnknownGenre`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `404 Not Found`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Movies not found for the specified genre"
     }
     ```

### Esempio 4: Aggiunta di un Film con Dati Non Validi

1. **Richiesta**: Tentativo di aggiungere un nuovo film con dati non validi
   - **Metodo HTTP**: `POST`
   - **URL**: `/addmovie`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     {
       "title": "New Movie",
       "director": "Invalid Director Name",
       "year": 1800,
       "genres": "Unknown Genre",
       "runtime": "not_a_number min",
       "original_language": "Invalid Language",
       "rating": "Invalid Rating"
     }
     ```
2. **Risposta**:
   - **Status Code**: `400 Bad Request`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "The year is not correct"
     }
     ```

### Esempio 5: Eliminazione di un Film con ID Non Esistente

1. **Richiesta**: Tentativo di eliminare un film con un ID non esistente nel database
   - **Metodo HTTP**: `DELETE`
   - **URL**: `/movie/9999`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     ```
2. **Risposta**:
   - **Status Code**: `404 Not Found`
   - **Corpo della Risposta**:
     ```json
     {
       "message": "Movie not found"
     }
     ```

### Descrizione dei Dati Attesi/Ottenuti in Caso di Errore

1. **Recupero Film per Decennio con Formato Errato**:
   - **Dati Attesi**: Parametro del decennio con formato errato.
   - **Dati Ottenuti**: Messaggio di errore che indica un formato di decennio non valido.

2. **Ordinamento Film con Direzione Errata**:
   - **Dati Attesi**: Direzione di ordinamento non valida (`invalid_direction`).
   - **Dati Ottenuti**: Messaggio di errore che indica un parametro di ordinamento non valido.

3. **Recupero Film per Genere Non Esistente**:
   - **Dati Attesi**: Parametro di un genere non presente nel database.
   - **Dati Ottenuti**: Messaggio di errore che indica che non sono stati trovati film per il genere specificato.

4. **Aggiunta di un Film con Dati Non Validi**:
   - **Dati Attesi**: Dati del film non validi nel corpo della richiesta.
   - **Dati Ottenuti**: Messaggio di errore che indica quali campi sono invalidi.

5. **Eliminazione di un Film con ID Non Esistente**:
   - **Dati Attesi**: ID del film non presente nel database.
   - **Dati Ottenuti**: Messaggio di errore che indica che il film non è stato trovato.


### Esempio 1: Aggiunta di una Lista di Film all'Endpoint `/movielist`

1. **Richiesta**: Aggiungere una lista di nuovi film al database
   - **Metodo HTTP**: `POST`
   - **URL**: `/movielist`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     [
       {
         "title": "Inception",
         "director": "Christopher Nolan",
         "year": 2010,
         "genres": "Action, Sci-Fi, Thriller",
         "runtime": "148 min",
         "original_language": "English",
         "rating": "8.8"
       },
       {
         "title": "The Matrix",
         "director": "Lana Wachowski, Lilly Wachowski",
         "year": 1999,
         "genres": "Action, Sci-Fi",
         "runtime": "136 min",
         "original_language": "English",
         "rating": "8.7"
       }
     ]
     ```
2. **Risposta**:
   - **Status Code**: `201 Created`
   - **Corpo della Risposta**:
     ```json
     {
       "movies": [
         {
           "id": 1,
           "title": "Inception",
           "director": "Christopher Nolan",
           "year": 2010,
           "genres": "Action, Sci-Fi, Thriller",
           "runtime": "148 min",
           "original_language": "English",
           "rating": "8.8"
         },
         {
           "id": 2,
           "title": "The Matrix",
           "director": "Lana Wachowski, Lilly Wachowski",
           "year": 1999,
           "genres": "Action, Sci-Fi",
           "runtime": "136 min",
           "original_language": "English",
           "rating": "8.7"
         }
       ]
     }
     ```

### Esempio 2: Aggiunta di una Lista di Film con Errori all'Endpoint `/movielist`

1. **Richiesta**: Aggiungere una lista di nuovi film con alcuni dati non validi
   - **Metodo HTTP**: `POST`
   - **URL**: `/movielist`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     [
       {
         "title": "Inception",
         "director": "Christopher Nolan",
         "year": 2010,
         "genres": "Action, Sci-Fi, Thriller",
         "runtime": "148 min",
         "original_language": "English",
         "rating": "8.8"
       },
       {
         "title": "Unknown Film",
         "director": "Invalid Director",
         "year": 1800,
         "genres": "Unknown Genre",
         "runtime": "not_a_number min",
         "original_language": "Invalid Language",
         "rating": "Invalid Rating"
       }
     ]
     ```
2. **Risposta**:
   - **Status Code**: `207 Multi-Status`
   - **Corpo della Risposta**:
     ```json
     {
       "movies": [
         {
           "id": 1,
           "title": "Inception",
           "director": "Christopher Nolan",
           "year": 2010,
           "genres": "Action, Sci-Fi, Thriller",
           "runtime": "148 min",
           "original_language": "English",
           "rating": "8.8"
         }
       ],
       "error_messages": [
         "Error adding movie 'Unknown Film': The year is not correct"
       ]
     }
     ```

### Esempio 3: Aggiunta di una Lista di Film Non Validi all'Endpoint `/movielist`

1. **Richiesta**: Tentativo di aggiungere una lista di nuovi film, tutti con dati non validi
   - **Metodo HTTP**: `POST`
   - **URL**: `/movielist`
   - **Headers**: 
     ```
     Authorization: Bearer <JWT_TOKEN>
     Content-Type: application/json
     ```
   - **Corpo della Richiesta**:
     ```json
     [
       {
         "title": "Invalid Movie 1",
         "director": "Invalid Director 1",
         "year": 1800,
         "genres": "Unknown Genre",
         "runtime": "not_a_number min",
         "original_language": "Invalid Language",
         "rating": "Invalid Rating"
       },
       {
         "title": "Invalid Movie 2",
         "director": "Invalid Director 2",
         "year": 1801,
         "genres": "Another Unknown Genre",
         "runtime": "not_a_number min",
         "original_language": "Another Invalid Language",
         "rating": "Another Invalid Rating"
       }
     ]
     ```
2. **Risposta**:
   - **Status Code**: `400 Bad Request`
   - **Corpo della Risposta**:
     ```json
     {
       "error_messages": [
         "Error adding movie 'Invalid Movie 1': The year is not correct",
         "Error adding movie 'Invalid Movie 2': The year is not correct"
       ]
     }
     ```

### Descrizione dei Dati Attesi/Ottenuti

1. **Aggiunta di una Lista di Film**:
   - **Dati Attesi**: Lista di film validi nel corpo della richiesta.
   - **Dati Ottenuti**: Lista di film appena aggiunti.

2. **Aggiunta di una Lista di Film con Errori**:
   - **Dati Attesi**: Lista di film con alcuni dati non validi.
   - **Dati Ottenuti**: Lista di film aggiunti con messaggi di errore per quelli non validi.

3. **Aggiunta di una lista di film con dati non validi**:
- **Dati Attesi**: Lista di film non validi nel corpo della richiesta.
- **Dati Ottenuti**: Messaggi di errore che spiegano perché ogni film non è stato aggiunto.