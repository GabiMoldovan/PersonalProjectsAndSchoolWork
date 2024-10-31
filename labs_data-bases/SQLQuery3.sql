USE lab1_firma;

/*
INSERT INTO adresa(id_adresa, tara, judet, oras, strada, numar_strada, cod_postal) VALUES (1, 'Romania', 'Cluj', 'Cluj-Napoca', 'Soarelui', 52, 5534526)
INSERT INTO adresa(id_adresa, tara, judet, oras, strada, numar_strada, cod_postal) VALUES (2, 'Romania', 'Cluj', 'Cluj-Napoca', 'Fabricii', 78, 5575314)
INSERT INTO adresa(id_adresa, tara, judet, oras, strada, numar_strada, cod_postal) VALUES (3, 'Romania', 'Cluj', 'Cluj-Napoca', 'Florilor', 14, 5532672)
INSERT INTO Firma(id_firma, id_adresa, nume_firma, fondator, email, nr_angajati, data_fondare) VALUES (1, 1, 'Vericu SRL', 'Vericu', 'vericu@gmail.com', 25, '2001-11-11')
INSERT INTO Magazin(id_magazin, id_firma, id_adresa, numar_angajati, nume) VALUES (1, 1, 1, 7, 'La Vericu')
INSERT INTO Magazin(id_magazin, id_firma, id_adresa, numar_angajati, nume) VALUES (2, 1, 2, 18, 'Vericu Accesorii')
INSERT INTO Provider(id_provider, id_adresa) VALUES (1, 1)
INSERT INTO firma_provider(id_firma, id_provider) VALUES (1, 1)
*/

SELECT * FROM Firma
SELECT * FROM adresa
SELECT * FROM Magazin
SELECT * FROM Provider
SELECT * FROM firma_provider


SELECT strada FROM adresa
UNION
SELECT nume FROM Magazin


SELECT DISTINCT Magazin.id_adresa, Magazin.nume FROM Magazin
INNER JOIN adresa ON Magazin.id_adresa = 2

SELECT Magazin.nume FROM Magazin
INNER JOIN Firma ON Firma.id_firma = 1


SELECT firma_provider.id_firma FROM firma_provider
LEFT JOIN Firma ON firma.id_firma = firma_provider.id_firma

SELECT SUM(numar_angajati), nume FROM Magazin
GROUP BY nume
HAVING SUM(numar_angajati) > 10

SELECT AVG(numar_angajati) FROM Magazin
GROUP BY nume

SELECT SUM(numar_angajati) from Magazin
GROUP BY id_firma

/*
DELETE FROM Firma
DELETE FROM adresa
DELETE FROM Magazin
DELETE FROM Provider
DELETE FROM firma_provider
*/

/*
UPDATE Magazin set nume = 'Accesorii Vericu' where id_magazin = 2
UPDATE adresa set strada = 'Smecherilor' where id_adresa = 2
*/

/*
DELETE FROM Magazin WHERE id_magazin = 2
*/