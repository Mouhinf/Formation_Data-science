CREATE TABLE client (
    client_id INT PRIMARY KEY,
    nom VARCHAR,
    numero VARCHAR
);

CREATE TABLE produit (
    produit_id INT PRIMARY KEY,
    nom_produit VARCHAR,
    categorie VARCHAR,
    prix INT
);

CREATE TABLE ordre (
    client_id INT,
    produit_id INT,
    ordre_date DATE,
    quantite INT,
    total INT,
    PRIMARY KEY (client_id, produit_id, ordre_date),
    FOREIGN KEY (client_id) REFERENCES client(client_id),
    FOREIGN KEY (produit_id) REFERENCES produit(produit_id)
);

INSERT INTO client (client_id, nom, numero) VALUES
(1, 'Client A', '771234567'),
(2, 'Client B', '776543213'),
(3, 'Client C', '781122333');

INSERT INTO produit (produit_id, nom_produit, categorie, prix) VALUES
(1, 'widget', 'Cat1', 10500),
(2, 'gadget', 'Cat2', 25000),
(3, 'bidule', 'Cat1', 30000);

INSERT INTO ordre (client_id, produit_id, ordre_date, quantite, total) VALUES
(1, 1, '2024-07-01', 2, 21000),
(1, 2, '2024-07-02', 1, 25000),
(2, 2, '2024-07-03', 1, 25000),
(3, 1, '2024-07-04', 1, 10500),
(3, 3, '2024-07-05', 2, 60000);

