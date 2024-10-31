USE lab3
GO
/*
INSERT INTO Categorie(id_cat, nume, descriere) VALUES (111, 'jurnal', 'desc jurnal');
INSERT INTO Categorie(id_cat, nume, descriere) VALUES (122, 'conferinte', 'desc conf');

INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (2919, 'titlu 1', 'abstract 1', 'autor 1', 122);
INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (3310, 'titlu 2', 'abstract 2', 'autor 2', 111);

INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (2920, 'titlu 3', 'abstract 2', 'autor 1', 122);
INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (2921, 'titlu 4', 'abstract 2', 'autor 1', 122);
INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (3311, 'titlu 5', 'abstract 1', 'autor 3', 111);
INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (2922, 'titlu 6', 'abstract 2', 'autor 4', 122);
INSERT INTO Publicatie(id_publ, titlu, abstract, autorp, id_cat) VALUES (2923, 'titlu 7', 'abstract 2', 'autor 4', 122);

INSERT INTO Biblioteca(id_biblio, nume, site) VALUES (101, 'ACM', 'www.acm.ro');
INSERT INTO Biblioteca(id_biblio, nume, site) VALUES (335, 'DBLP', 'www.dblp.ro');

INSERT INTO Indexare(id_publ, id_biblio) VALUES (2919, 335)
INSERT INTO Indexare(id_publ, id_biblio) VALUES (3310, 101)
INSERT INTO Indexare(id_publ, id_biblio) VALUES (3311, 101)
*/
/*
DELETE FROM Categorie
DELETE FROM Publicatie
DELETE FROM Biblioteca
*/



-- 1

-- Numele autorilor principali care au publicat in jurnal sau in conferinte
SELECT P.autorp from Publicatie P 
inner join Categorie C on P.id_cat = C.id_cat WHERE C.nume = 'jurnal' 
UNION 
SELECT P.autorp FROM Publicatie P 
inner join Categorie C on P.id_cat = C.id_cat WHERE C.nume = 'conferinte'



-- 2 

-- Numele autorilor principali indexati in bibl electronica cu numele 'DBLP'
SELECT Publicatie.autorp from Publicatie 
inner join Indexare on Publicatie.id_publ = Indexare.id_publ 
inner join Biblioteca on Indexare.id_biblio = Biblioteca.id_biblio 
WHERE Biblioteca.nume = 'DBLP'


-- Site-ul web si numele bibl care indexeaza publ stiintifice din categ cu numele jurnal
SELECT DISTINCT Biblioteca.site, Biblioteca.nume from Biblioteca 
inner join Indexare on Biblioteca.id_biblio = Indexare.id_biblio 
inner join Publicatie on Indexare.id_publ = Publicatie.id_publ 
inner join Categorie on Publicatie.id_cat = Categorie.id_cat 
WHERE Categorie.nume = 'jurnal'

-- Titlul si numele bibliotecii pt toate publicatiile indiferent daca sunt indexate sau nu intr-o biblioteca
SELECT Publicatie.titlu, Biblioteca.nume from Publicatie 
left join Indexare on Indexare.id_publ = Publicatie.id_publ 
inner join Biblioteca on Biblioteca.id_biblio = Indexare.id_biblio

-- 3

-- Autorii care au cel putin doua publicatii
SELECT Publicatie.autorp, COUNT(Publicatie.autorp) as 'count' from Publicatie GROUP BY Publicatie.autorp HAVING COUNT(Publicatie.autorp) > 1
ORDER BY COUNT(Publicatie.autorp) DESC;

-- Autorii care au cel putin o publicatie din categoria 'jurnal'
SELECT Publicatie.autorp, Publicatie.id_cat, COUNT(Publicatie.autorp) as 'count' from Publicatie 
WHERE Publicatie.id_cat = 111 
GROUP BY Publicatie.autorp, Publicatie.id_cat 
HAVING COUNT(Publicatie.autorp) >= 1
ORDER BY COUNT(Publicatie.autorp) DESC;

-- Autorii in dupa numarul publicatiilor
SELECT Publicatie.autorp, COUNT(Publicatie.autorp) as 'count' from Publicatie GROUP BY Publicatie.autorp
ORDER BY COUNT(Publicatie.autorp) DESC;