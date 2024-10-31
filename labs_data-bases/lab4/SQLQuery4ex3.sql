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