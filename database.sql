CREATE TABLE categorie (
    num_categoria INTEGER PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE spese (
    num_spesa INTEGER PRIMARY KEY,
    data_spesa DATE NOT NULL,
    importo DECIMAL(10,2) NOT NULL CHECK(importo > 0),
    descrizione VARCHAR(255),
    num_categoria INTEGER NOT NULL,

    FOREIGN KEY (num_categoria)
        REFERENCES categorie(num_categoria)
);

CREATE TABLE budget (
    num_budget INTEGER PRIMARY KEY,
    mese VARCHAR(7) NOT NULL,
    importo_budget DECIMAL(10,2) NOT NULL CHECK(importo_budget > 0),
    num_categoria INTEGER NOT NULL,

    FOREIGN KEY (num_categoria)
        REFERENCES categorie(num_categoria),

    UNIQUE(mese, num_categoria)
);


INSERT INTO categorie (num_categoria, nome_categoria)
VALUES
(1, 'Alimentari'),
(2, 'Vacanze'),
(3, 'Svago'),
(4, 'Casa');


INSERT INTO spese
(num_spesa, data_spesa, importo, descrizione, num_categoria)
VALUES
(1, '2026-01-05', 35.50, 'Spesa supermercato', 1),
(2, '2026-01-10', 600.00, 'Viaggio a Santorini', 2),
(3, '2026-01-15', 20.00, 'Pokemon', 3);


INSERT INTO budget
(num_budget, mese, importo_budget, num_categoria)
VALUES
(1, '2026-01', 300.00, 1),
(2, '2026-01', 1000.00, 2),
(3, '2026-01', 80.00, 3);
