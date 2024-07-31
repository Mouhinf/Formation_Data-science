/* ENREGISTREMENT */

/* LA TABLE PRODUIT */
INSERT INTO produits (nom, prix) VALUES ('Cookies', 10);
INSERT INTO produits (nom, prix) VALUES ('Candy', 5.2);

/* LA TABLE CLIENT */
INSERT INTO clients (nom, adresse) VALUES ('Ahmed', 'Tunisie');
INSERT INTO clients (nom, adresse) VALUES ('Coulibaly', 'Sénégal');
INSERT INTO clients (nom, adresse) VALUES ('Hasan', 'Egypte');

/* LA TABLE COMMANDE */
INSERT INTO commandes (costumerid, productid, quantite, order_date) VALUES (1, 2, 3, '2023-01-22');
INSERT INTO commandes (costumerid, productid, quantite, order_date) VALUES (2, 1, 10, '2023-04-14');

/* Mise à jour de la quantite de la deuxieme commande */
UPDATE commandes
SET quantite = 6
WHERE costumerid = 2 AND productid = 1 AND order_date = '2023-04-14';

/* Suppression du troisième client de la table clients */
DELETE FROM clients
WHERE nom = 'Hasan' AND adresse = 'Egypte';

/* Supression du contenu de la table commandes */
DELETE FROM commandes;

/* Suppression entière de la table commandes */
DROP TABLE commandes;
