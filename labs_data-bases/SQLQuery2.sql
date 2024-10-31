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