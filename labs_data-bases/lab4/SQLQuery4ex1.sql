USE lab1_firma
GO

CREATE OR ALTER PROCEDURE adaugaFirma(@id_firma int, @id_adresa int, @nume_firma nvarchar(16), @fondator nvarchar(32), @email nvarchar(32), @nr_angajati int, @data_fondare date) as
BEGIN
DECLARE @id int
SET @id = (SELECT COUNT(*) FROM Firma WHERE id_firma = @id_firma)
if @id != 0
    RAISERROR('Exista deja acest id!', 10,1)
else if @nr_angajati = 0
    RAISERROR('Firma nu poate avea 0 angajati!', 5,0)
else
    INSERT INTO Firma VALUES(@id_firma, @id_adresa, @nume_firma, @fondator, @email, @nr_angajati, @data_fondare)
END
GO

-- EXEC adaugaFirma @id_firma = 2, @id_adresa = 1, @nume_firma = 'test', @fondator = 'testare', @email = 'testare@gmail.com', @nr_angajati = 0, @data_fondare = '11.11.2022';
-- GO
--SELECT * FROM Firma