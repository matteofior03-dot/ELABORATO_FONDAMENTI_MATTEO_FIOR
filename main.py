import sqlite3
import os

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Attiva i controlli FOREIGN KEY
cursor.execute("PRAGMA foreign_keys = ON")

# Carica il file database.sql solo se il database è vuoto
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='categorie'")
tabella_esiste = cursor.fetchone()

if tabella_esiste is None:
    if os.path.exists("database.sql"):
        with open("database.sql", "r", encoding="utf-8") as file:
            script_sql = file.read()
            cursor.executescript(script_sql)
            conn.commit()
            print("Database creato usando database.sql")
    else:
        print("Errore: file database.sql non trovato.")


while True:
    print("Benvenuto nel programma di gestione delle spese personali")
    print("-------------------------")
    print("SISTEMA SPESE PERSONALI")
    print("-------------------------")
    print("1. Gestione Categorie")
    print("2. Inserisci Spesa")
    print("3. Definisci Budget Mensile")
    print("4. Visualizza Report")
    print("5. Esci")
    print("-------------------------")

    scelta = input("Inserisci la tua scelta: ")

    if scelta == "1":
        num_categoria = int(input("Numero categoria: "))
        nome_categoria = input("Nome categoria: ")

        try:
            cursor.execute(
                "INSERT INTO categorie (num_categoria, nome_categoria) VALUES (?, ?)",
                (num_categoria, nome_categoria)
            )
            conn.commit()
            print("Categoria inserita correttamente.")
        except sqlite3.IntegrityError:
            print("Errore: la categoria esiste gia'.")

    elif scelta =="2":
        num_spesa=int(input("Numero spesa:"))
        data_spesa=input("Data spesa (formato YYYY-MM-DD)")
        importo=float(input("Importo"))
        if importo<=0:
            print("L'importo deve essere maggiore di 0")
            while importo <=0:
                importo=float(input("Inserire correttamente importo"))
        descrizione=input("Descrizione (facoltativa)")
        #num_categoria=int(input("Numero categoria"))
        nome_categoria=input("Nome categoria:")

        cursor.execute(
            "SELECT num_categoria FROM categorie WHERE nome_categoria = ?",
        (nome_categoria,)
        )
        categoria=cursor.fetchone()


        if categoria is None:
            print("Categoria non esiste.")
        else:
            num_categoria=categoria[0]
            try:
                cursor.execute(
                    """INSERT INTO spese (num_spesa, data_spesa, importo, descrizione, num_categoria) VALUES (?, ?, ?, ?, ?)""",
                    (num_spesa, data_spesa, importo,
                     descrizione, num_categoria)
                )

                conn.commit()

                print("Spesa inserita correttamente.")

            except sqlite3.IntegrityError:
                print("Il numero della spesa è già esistente")


    elif scelta=="3":
        mese=input("Inserisci il mese (YYYY-MM):")
        nome_categoria=input("Nome categoria:")
        importo_budget=float(input("Importo budget:"))
        num_budget=int(input("Numero budget:"))

        if importo_budget<=0:
            print("L'importo deve essere maggiore di 0")
            while importo_budget <=0:
                importo=float(input("Inserire correttamente importo"))
        else:
            cursor.execute(
                "SELECT num_categoria FROM categorie WHERE nome_categoria = ?",
                (nome_categoria,)
            )
            categoria = cursor.fetchone()
            if categoria is None:
                print("Categoria non esiste.")
            else:
                num_categoria = categoria[0]

                try:
                    cursor.execute(
                        """INSERT INTO budget(num_budget, mese, importo_budget, num_categoria)VALUES (?, ?, ?, ?)""",
                        (num_budget, mese, importo_budget, num_categoria)
                    )

                    conn.commit()
                    print("Budget inserito correttamente")
                    print(importo_budget)

                except sqlite3.IntegrityError:
                    print("Errore budget")

    elif scelta=="4":
        while(True):
            print("Menu dei report")
            print("1.Totale spese per categoria\n2.Spese mensili vs budget\n3.Elenco completo delle spese ordinate per data\n4.Ritorna al menu principale")
            report=input("Inserire scelta:")
            if report=="1":
                cursor.execute(
                    """SELECT categorie.nome_categoria,SUM(spese.importo)FROM categorie INNER JOIN spese ON categorie.num_categoria=spese.num_categoria GROUP BY categorie.nome_categoria"""
                )
                print("Categoria.....Totale speso")
                for i in cursor.fetchall():
                    print(i[0],"......",i[1])


            elif report == "2":
                cursor.execute(
                    """ SELECT budget.mese, SUM(budget.importo_budget) AS budget_totale,
                    COALESCE((SELECT SUM(spese.importo)
                    FROM spese WHERE substr(spese.data_spesa, 1, 7) = budget.mese), 0) AS totale_spese
                    FROM budget
                    GROUP BY budget.mese
                    """
                )

                for i in cursor.fetchall():
                    print("--------")
                    print("Mese:", i[0])
                    print("Budget totale:", i[1])
                    print("Totale spese:", i[2])

                    if i[2] > i[1]:
                        print("Stato: SUPERAMENTO BUDGET")
                    else:
                        print("Stato: BUDGET NON SUPERATO")

                        print("--------")

            elif report=="3":
                cursor.execute(
                    """SELECT spese.data_spesa,categorie.nome_categoria,spese.importo,spese.descrizione FROM categorie INNER JOIN spese ON categorie.num_categoria=spese.num_categoria
                    ORDER BY spese.data_spesa DESC"""
                )

                for i in cursor.fetchall():
                    print("--------")
                    print("Data","       Categoria  Importo    Descrizione")
                    print("-----------------------------------------------")
                    print(i[0]," ",i[1]," ",i[2]," ",i[3])

            if report=="4":
                break


    elif scelta == "5":
        print("Il programma è stato chiuso correttamente")
        break

    else:
         print("Scelta non valida. Riprovare.")

conn.close()
