SELECT TOP (1000) [ID]
      ,[Frase_Español]
      ,[Frase_Inglés]
  FROM [DDFRASES].[dbo].[DD_Lines]

  CREATE TABLE Frases_Unificadas (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Frase_Espanol NVARCHAR(500) NOT NULL,
    Frase_Ingles NVARCHAR(500) NOT NULL
);
INSERT INTO Frases_Unificadas (Frase_Espanol, Frase_Ingles)
SELECT frases_español, frases_inglés FROM Frases_Oraculo
UNION
SELECT Frase_Español, Frase_Inglés FROM DD_Lines;

DROP TABLE Frases_Oraculo;
DROP TABLE DD_Lines;


EXEC sp_rename 'Frases_Unificadas', 'Frases_Oraculo';

EXEC sp_rename 'Frases_Oraculo.ID', 'ID_Key', 'COLUMN';

ALTER TABLE Frases_Oraculo ADD ID_Origen AS ('DD' + CAST(ID_Key AS VARCHAR(10)));

