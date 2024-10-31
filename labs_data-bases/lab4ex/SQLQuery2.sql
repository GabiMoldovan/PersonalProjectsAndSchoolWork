USE filmm
GO


/*
CREATE OR ALTER PROCEDURE SelectAllFilms AS
SELECT * FROM filmm;


EXEC SelectAllFilms
*/

/*
CREATE OR ALTER PROCEDURE SelectFilmsByCountry @Country nvarchar(10) AS
SELECT * FROM filmm
WHERE Country = @Country;

EXEC SelectFilmsByCountry @Country = "USA"
*/

/*
CREATE OR ALTER PROCEDURE SelectFilmsByCountry @Country nvarchar(10), @Name nvarchar(100) AS
SELECT * FROM filmm
WHERE Country = @Country
AND Title = @Name;

EXEC SelectFilmsByCountry @Country = "USA", @Name = "Film F";
EXEC SelectFilmsByCountry "USA", "Film F"
*/

/*

CREATE OR ALTER VIEW [Films from USA] AS
SELECT * From filmm
WHERE Country = 'USA';

*/


CREATE OR ALTER TRIGGER t_filmm_insert ON filmm INSTEAD OF INSERT
AS BEGIN
	DECLARE @id INT;
	Declare @title NVARCHAR(100);
	DECLARE @year DATE;
	DECLARE @country NVARCHAR(10);

	SELECT @id = ID, @title = Title, @year = Year, @country = Country FROM INSERTED;

	IF @id IS NULL
		THROW 51000, 'cannot insert film without id', 1;

	IF @year IS NULL
		SET @year = '2001-01-01';
	
	INSERT INTO filmm(ID, Title, Year, Country) VALUES (@id, @title, @year, @country);
END;
