# ELABORATO_FONDAMENTI_MATTEO_FIOR

Ambiente di sviluppo
Il progetto è stato sviluppato e testato utilizzando PyCharm, un ambiente di sviluppo integrato per Python. Tuttavia, il programma può essere eseguito anche tramite una normale installazione di Python senza l’utilizzo di PyCharm.
 
Requisiti
•           Python 3.x
•           PyCharm (opzionale)
•           Librerie standard utilizzate:
•           sqlite3
•           os
Non sono richieste installazioni aggiuntive.
 
Esecuzione tramite PyCharm:
1.         Aprire il progetto in PyCharm.
2.         Verificare che i file main.py e database.sql siano presenti nella stessa cartella del progetto.
3.         Aprire il file main.py.
4.         Eseguire il programma tramite il pulsante Run oppure con click destro su main.py → Run ‘main’.
5.         Al primo avvio il programma creerà automaticamente il database SQLite e mostrerà il menu principale.
 
Esecuzione tramite Python da terminale:
1.         Salvare i file main.py e database.sql nella stessa cartella.
2.         Aprire il Prompt dei comandi da Windows (cmd)
3.         Spostarsi nella cartella in cui è stato salvato il progetto utilizzando il comando: cd nome_cartella 
Ad esempio, se è stato salvato nella cartella elaborato_studente nel Desktop il comando sarà:
 cd Desktop\elaborato_studente
4.         Verificare la presenza dei file di progetto tramite il comando: dir
Devono essere visibili almeno i file:
-          database.sql
-          main.py
5.         Eseguire il programma con il comando: python main.py
6.         ATTENZIONE: se il file è stato rinominato durante il download, ad esempio main (1).py, utilizzare il nome visualizzato a schermo e dunque eseguire come: python “main (1).py”
7.         Al primo avvio il programma creerà automaticamente il database SQLite e mostrerà il menu principale. 
 
 
File del progetto
        •       main.py → programma principale.
        •       database.sql → script SQL contenente la struttura del database e i dati di esempio.
        •       database.db → database SQLite generato automaticamente alla prima esecuzione del programma.
