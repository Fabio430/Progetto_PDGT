# API per la gestione di film

API che consente agli utenti di gestire una libreria virtuale di film, includendo operazioni come aggiunta(ok), modifica(ok) ed eliminazione di film(ok).
Puoi anche implementare funzionalità di ricerca(ok) e ordinamento(ok).

video 75(How to configure Flask-SQLAlchemy with your Flask app) udemy per creare il database

# __pycache__ -> ok
# .venv -> ok
# instance -> ok
# migrations
# models -> ok
# resources -> ok
# .env
# .env.example -> ok
# .flaskenv -> ok
# .gitignore
# app.py
# blocklist.py -> ok
# contributing.md -> ok
# db.py -> ok
# docker-entrypoint.sh -> ok
# Dockerfile
# readme.md -> ok
# requirements.txt -> ok
# schemas.py -> ok

cose da aggiungere all'API:
# - richiedere un access token per aggiungere e eliminare un film -> ok
# - richiedere un refresh token per le richieste get -> ok
# - aggiungere controllo stretto in modo da non permettere di aggiungere lo stesso film -> ok
# - aggiungere la modifica dei dati di un film -> ok
# - potrei aggiungere il controllo stretto per l'inserimento dell'anno. Per esempio dal 1895 al 2025 oppure semplicemente maggiore del 1895 -> ok
# - modificare la ricerca, l'eliminazione e la modifica in modo che utilizzi la stringa del titolo del film -> ok
# - aggiungere qualche altra funzionalità di ricerca, ordinamento, ecc.
# - aggiungere i route per il rating
- migliorare la sicurezza della chiave segreta -> ho generato una chiave più sicura. Quando faccio il deployment su render, faccio lo store della key come environment variable
# - fare i passaggi vari per il deployment dell'app

# - decidere se aggiungere o no la migrazione del database (no)
# - controllare gli HTTP status code in app.py, cioè i 401
# - controllare se cambiare le stringhe di informazione e i codici di errore (404, 409, ecc.)
- il file con la chiave credo di doverlo portare all'esame. Comunque devo controllare i file che devo portarmi tra quelli che aggiungo a .gitignore
  oppure semplicemente carico tutti i file nella repository pubblica di github, per esempio anche il .env(potrei chiedere alla prof), tanto alla fine 
  è un progetto per un esame --> posso mettere una nota in Readme.md dove scrivo che di solito file1, file2, ecc. dovrebbero essere aggiunti a .gitignore
  ma per semplicità li ho lasciati nella repository pubblica.
# - quando effettuo il logout, devo rimuovere anche il refresh token (fatto)
# - nella ricerca per decade, una stringa come questa: "2010ss" funziona. Quindi devo sistemare questo bug. (sistemato)
- documentare meglio il codice attraverso i commenti

# - potrei aggiungere un nuovo route DEL: elimina tutti i film della lista.
# - potrei aggiungere un nuovo route POST: aggiungi più film contemporaneamente, cioè aggiungi una lista di film.
# - mettere un limite al numero di film che è possibile aggiungere contemporaneamente.
- # director -> da sistemare, eliminare gli spazi bianchi prima e dopo, errore in caso di stringa vuota o vuota con più spazi
  # genres -> aggiungere un trattino per la parola science-fiction
  # original_language -> come per director
  # rating -> ok
  # runtime -> ok
  # title -> come per director e original language
  # year -> ok
# - migliorare il codice sostituendolo con funzioni laddove ci sono ripetizioni di codice.
# - provare a vedere se è possibile utilizzare i messaggi creati dagli abort nel route per aggiungere un singolo film alla volta all'interno del route per aggiungere più film alla volta