USE lab1_firma
GO

CREATE OR ALTER VIEW getAllMagazineFromFirma AS
SELECT Magazin.nume, Magazin.id_adresa from Magazin
INNER JOIN Firma on Magazin.id_firma = firma.id_firma
GO

-- SELECT *FROM getAllMagazineFromFirma