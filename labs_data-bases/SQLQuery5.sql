USE lab1_firma
GO

-- ex 1

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


CREATE OR ALTER PROCEDURE adaugaProvider(@id_provider int, @id_adresa int) as
BEGIN 
DECLARE @idprovider int
SET @idprovider = (SELECT COUNT(*) FROM Provider WHERE id_provider = @id_provider)
DECLARE @idadresa int
SET @idadresa = (SELECT COUNT(*) FROM adresa WHERE id_adresa = @id_adresa)
if @idprovider = 0
    RAISERROR('Nu exista provider-ul cu acest id!', 10,1)
else if @idadresa = 0
    RAISERROR('Nu exista adresa cu acest id!', 10,1)
else
    INSERT INTO Provider VALUES(@id_provider, @id_adresa)
END
GO


CREATE OR ALTER PROCEDURE adaugaFirma_Provider(@id_firma int, @id_provider int) as


BEGIN 
DECLARE @idprovider int
SET @idprovider = (SELECT COUNT(*) FROM Provider WHERE id_provider = @id_provider)
DECLARE @idfirma int
SET @idfirma = (SELECT COUNT(*) FROM Firma WHERE id_firma = @id_firma)
if @idprovider = 0
    RAISERROR('Nu exista provider-ul cu acest id!', 10,1)
else if @idfirma = 0
    RAISERROR('Nu exista o firma cu acest id!', 10,1)
else
    INSERT INTO Provider VALUES(@id_firma, @id_provider)
END
GO

-- EXEC adaugaFirma @id_firma = 2, @id_adresa = 1, @nume_firma = 'test', @fondator = 'testare', @email = 'testare@gmail.com', @nr_angajati = 0, @data_fondare = '11.11.2022';
-- GO
--SELECT * FROM Firma


--- end of ex1


-- ex 2

CREATE OR ALTER VIEW getAllMagazineFromFirma AS
SELECT Magazin.nume, Magazin.id_adresa from Magazin
INNER JOIN Firma on Magazin.id_firma = firma.id_firma
GO

-- end of ex2


-- SELECT *FROM getAllMagazineFromFirma


-- ex 3


USE [lab1_firma]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE OR ALTER TRIGGER [dbo].[Trigger1]
ON [dbo].[adresa]
FOR INSERT 
AS BEGIN 
DECLARE @id_adresa INT;
DECLARE @tara nvarchar(16);
DECLARE @judet nvarchar(16);
DECLARE @oras nvarchar(16);
DECLARE @strada nvarchar(16);
DECLARE @numar_strada INT;
DECLARE @cod_postal nvarchar(7);

DECLARE @time datetime;
DECLARE @type nvarchar(100);
DECLARE @table_name nvarchar(100);

SET @table_name = 'adresa';
SET @type = 'INSERT';
SET @time = CURRENT_TIMESTAMP;

SELECT id_adresa = @id_adresa, tara = @tara, judet = @judet, oras = @oras, strada = @strada, numar_strada = @numar_strada, cod_postal = @cod_postal FROM inserted;
if @id_adresa is not null
	INSERT INTO adresa(id_adresa, tara, judet, oras, strada, numar_strada, cod_postal) values (@id_adresa, @tara, @judet, @oras, @strada, @numar_strada, @cod_postal)
PRINT 'S-a adaugat coloana din tabelul '+ @table_name +' la data si ora '+ CONVERT(VARCHAR(20), @time,0) +' cu operatia de tipul '+ @type;
END;


GO
-- INSERT INTO adresa(id_adresa, tara, judet, oras, strada, numar_strada, cod_postal) VALUES (4, 'romania', 'cluj', 'cluj-napoca', 'nush', 10, '2563463')
GO
SELECT * FROM adresa

GO
USE [lab1_firma]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE OR ALTER   TRIGGER [dbo].[Trigger2]
ON [dbo].[adresa]
FOR DELETE
AS BEGIN 
DECLARE @id_adresa INT;
DECLARE @tara nvarchar(16)
DECLARE @judet nvarchar(16)
DECLARE @oras nvarchar(16)
DECLARE @strada nvarchar(16)
DECLARE @numar_strada INT
DECLARE @cod_postal nvarchar(7)
DECLARE @table_name nvarchar(16)
DECLARE @time datetime
DECLARE @type nvarchar(16)
DECLARE @count int
SET @table_name = 'adresa';
SELECT id_adresa = @id_adresa, time = @time, type = @type FROM deleted
	SET @time = CURRENT_TIMESTAMP
	SET @type = 'DELETE';
SELECT @count = COUNT(*) FROM adresa WHERE id_adresa = @id_adresa;
IF @count = 0
	DELETE FROM adresa WHERE id_adresa = @id_adresa;
ELSE
    THROW 51000, 'can not delete - country is referenced in other tables', 1;
PRINT 'S-a sters o coloana din tabelul '+ @table_name +' la data si ora '+ CONVERT(VARCHAR(20), @time,0) +' cu operatia '+ @type;
END;

GO
-- delete from adresa where id_adresa = 4
GO
select * from adresa