### Zadanie 1a.

Aplikacja została zrealizowana przy pomocy języka Python w wersji 3.11.9 oraz frameworka Django w wersji 5.0.4.
Serwer Django uruchamiany jest za pomocą polecenia "python manage.py runserver". Wystartowanie serwera bazowo
powoduje wyświetlenie informacji takich jak np. port serwera. W zadaniu zmodyfikowano
plik manage.py w następująćy sposób:

![image](https://github.com/BartoszKedziorek/PAwChO-Zadanie1/assets/104023013/8df863ef-1242-482d-bcc1-4ec278633d09)

Modyfikacja powoduje wyświetlenie żądanych informacji:

![image](https://github.com/BartoszKedziorek/PAwChO-Zadanie1/assets/104023013/1e2504da-11cf-4da5-b46c-0c7d2e81124d)


### Zadanie 1b.
W celu pobrania adresu IP klienta wykorzystano atrybut "META['REMOTE_ADDR']" z obietu żądania, utworzonego
automatycznie przez Django. Atrybut ten został przekazany do szablonu pliku html:

![image](https://github.com/BartoszKedziorek/PAwChO-Zadanie1/assets/104023013/c7b5142b-f6c6-44f1-96a9-8306e55ea000)

Strefa czasowa klienta oraz aktualny czas w strefie czasowej klienta zostaje pobierany po stronie klienta za
pomocą funkcji "getTimezone()". Funkcja ta uzupełnia odpowiednie elementy html zawartością:

![image](https://github.com/BartoszKedziorek/PAwChO-Zadanie1/assets/104023013/56a0f8b8-eea8-4564-b0fc-f1c0d074d67d)

### Zadanie 2.
Plik Dockerfile wraz z niezbędnymi komentarzami został umieszczony w repozytorium

### Zadanie 3a. Polecenie budujące obraz kontenera
```docker build -t local/zadanie1:test .```

### Zadanie 3b. Uruchomienie kontenera na postawie zbudowanego obrazu
```docker run -d  --name zadaniepierwsze -p 191:8000 local/zadanie1:test```

### Zadanie 3c. Sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera
W celu wyśwetlenia informacji z zadania 1a należy podczas uruchamiania kontenera
podłączyć terminal za pomocą flagi "-t"

```docker run -t  --name zadaniepierwsze -p 191:8000 local/zadanie1:test``` 

### Zadanie 3d. Sprawdzenie liczby warstw
```docker inspect local/zadanie1:test```

### Zadanie 3*. Zrzut ekranu
![image](https://github.com/BartoszKedziorek/PAwChO-Zadanie1/assets/104023013/eda09cd0-0e84-4ea8-be13-842db30f129f)
