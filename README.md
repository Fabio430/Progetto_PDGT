- Nome: Fabio, cognome: Giannoccoli, matricola: 279044
- Titolo del progetto: Movies API
- Breve relazione:
# 1. Descrizione del servizio implementato e del suo scopo
Il progetto consiste in un servizio web chiamato Movies API, progettato per gestire e fornire informazioni su una libreria virtuale di film. Gli utenti possono registrarsi, autenticarsi e compiere varie operazioni, nello specifico:
1. Aggiungere un nuovo film.
2. Aggiungere più film contemporaneamente (limite impostato a 200).
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
La comunicazione tra i vari componenti dell'applicazione avviene tramite HTTP. Il client invia richieste HTTP al server Flask, che processa queste richieste, interagisce con il database PostgreSQL tramite SQLAlchemy, e restituisce una risposta al client. Le API seguono lo stile RESTful, il che facilita l'integrazione con diversi tipi di client, come applicazioni web, mobile, o altri servizi.

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
Il file blocklist.py viene utilizzato per fare lo store degli access token e dei refresh token non più validi. Il file refresh_token_store.py invece viene utilizzato per fare lo store momentaneo del refresh token. Sono stati utilizzati dei file locali per semplicità ma probabilmente questa non è la scelta migliore né la più sicura.

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