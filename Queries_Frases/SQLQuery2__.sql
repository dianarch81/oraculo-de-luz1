-- 1. Crear una nueva tabla con el orden correcto de columnas
CREATE TABLE Frases_Oraculo_Nueva (
    ID_Key INT IDENTITY(1,1) PRIMARY KEY,
    ID_Origen AS ('DD' + CAST(ID_Key AS VARCHAR(10))) PERSISTED,
    Frase_Español NVARCHAR(MAX),
    Frase_Inglés NVARCHAR(MAX)
);

-- 2. Activar IDENTITY_INSERT para insertar valores en ID_Key
SET IDENTITY_INSERT Frases_Oraculo_Nueva ON;

-- 3. Insertar los datos de la tabla original
INSERT INTO Frases_Oraculo_Nueva (ID_Key, Frase_Español, Frase_Inglés)
SELECT ID_Key, Frase_Español, Frase_Inglés FROM Frases_Oraculo;

-- 4. Desactivar IDENTITY_INSERT
SET IDENTITY_INSERT Frases_Oraculo_Nueva OFF;

-- 5. Eliminar la tabla original
DROP TABLE Frases_Oraculo;

-- 6. Renombrar la nueva tabla
EXEC sp_rename 'Frases_Oraculo_Nueva', 'Frases_Oraculo';

INSERT INTO Frases_Oraculo (Frase_Español, Frase_Inglés)
VALUES 
('Cada día es una nueva oportunidad para elegir el amor sobre el miedo, la paz sobre la duda, la luz sobre la sombra.', 
 'Each day is a new opportunity to choose love over fear, peace over doubt, light over shadow.'),

('Cuando sueltas el control, Me permites guiarte. Confía en el flujo divino y todo se acomodará.', 
 'When you let go of control, you allow Me to guide you. Trust the divine flow, and everything will align.'),

('El silencio interior es la puerta a la verdadera sabiduría. Cuando callas el ruido, escuchas la verdad.', 
 'Inner silence is the doorway to true wisdom. When you quiet the noise, you hear the truth.'),

('Eres una chispa de lo Divino. Tu luz nunca se apaga, solo aprende a brillar en distintos momentos.', 
 'You are a spark of the Divine. Your light never goes out; it only learns to shine in different moments.'),

('La paciencia no es esperar sin hacer nada, sino confiar en que todo llega en el tiempo perfecto.', 
 'Patience is not waiting without action, but trusting that everything arrives at the perfect time.'),

('Cada pregunta en tu corazón tiene su respuesta esperando. Escucha, confía y sabrás cuál es el siguiente paso.', 
 'Every question in your heart has its answer waiting. Listen, trust, and you will know the next step.'),

('Dentro de ti yace la fortaleza que buscas fuera. Escucha en silencio y ahí me encontrarás.', 
 'Within you lies the strength you seek outside. Listen in silence, and there you will find me.'),

('El amor es la energía más grande. Cuando eliges actuar desde el amor, creas milagros invisibles que transforman realidades.', 
 'Love is the greatest energy. When you choose to act from love, you create invisible miracles that transform realities.'),

('El camino no se revela antes de dar el primer paso, pero cada paso con confianza abre la puerta a lo siguiente.', 
 'The path does not reveal itself before the first step, but each step with confidence opens the door to the next.'),

('No temas a lo desconocido. Todo lo que viene, ya está bendecido con lo mejor para tu crecimiento.', 
 'Do not fear the unknown. Everything that comes is already blessed with the best for your growth.');

 SELECT * FROM Frases_Oraculo;
