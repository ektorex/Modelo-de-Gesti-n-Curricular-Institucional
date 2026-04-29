-- =========================
-- CARRERAS
-- =========================
INSERT INTO carreras (clave, nombre, fecha_alta, fecha_baja) VALUES
('PEND', 'SIN CARRERA ASIGNADA', '2010-01-01', NULL), -- IMPORTANTE Campo al que le relacionan planes sin carreras 
('ISC', 'Ingenieria en Sistemas Computacionales', '2010-01-01', NULL),
('IIA', 'Ingenieria en Inteligencia Artificial', '2020-01-01', NULL),
('IMEC', 'Ingenieria Mecatronica', '2012-01-01', NULL);

-- =========================
-- MATERIAS
-- =========================
INSERT INTO materias (clave, nombre, fecha_alta, fecha_baja, semestre) VALUES
-- Sem 1
('MAT1', 'Calculo Diferencial', '2010-01-01', NULL, 1),
('PROG1', 'Fundamentos de Programacion', '2010-01-01', NULL, 1),
('LOG1', 'Logica Matematica', '2010-01-01', NULL, 1),

-- Sem 2
('MAT2', 'Calculo Integral', '2010-01-01', NULL, 2),
('PROG2', 'Programacion Orientada a Objetos', '2010-01-01', NULL, 2),
('EST1', 'Probabilidad y Estadistica', '2010-01-01', NULL, 2),

-- Sem 3
('MAT3', 'Algebra Lineal', '2010-01-01', NULL, 3),
('ED1', 'Estructuras de Datos', '2010-01-01', NULL, 3),
('BD1', 'Bases de Datos', '2010-01-01', NULL, 3),

-- Sem 4
('SO1', 'Sistemas Operativos', '2010-01-01', NULL, 4),
('RED1', 'Redes de Computadoras', '2010-01-01', NULL, 4),
('IA1', 'Introduccion a la Inteligencia Artificial', '2020-01-01', NULL, 4),

-- Sem 5
('IA2', 'Aprendizaje Automatico', '2020-01-01', NULL, 5),
('BD2', 'Bases de Datos Avanzadas', '2010-01-01', NULL, 5),
('SO2', 'Sistemas Distribuidos', '2010-01-01', NULL, 5);

-- =========================
-- PREREQUISITOS
-- =========================
INSERT INTO prerequisitos (materia_clave, requisito_clave) VALUES
-- MAT2 requiere MAT1
('MAT2', 'MAT1'),

-- PROG2 requiere PROG1
('PROG2', 'PROG1'),

-- EST1 requiere MAT1
('EST1', 'MAT1'),

-- MAT3 requiere MAT2
('MAT3', 'MAT2'),

-- ED1 requiere PROG2
('ED1', 'PROG2'),

-- BD1 requiere PROG2
('BD1', 'PROG2'),

-- SO1 requiere ED1
('SO1', 'ED1'),

-- RED1 requiere ED1
('RED1', 'ED1'),

-- IA1 requiere MAT3 y EST1
('IA1', 'MAT3'),
('IA1', 'EST1'),

-- IA2 requiere IA1, MAT3, EST1
('IA2', 'IA1'),
('IA2', 'MAT3'),
('IA2', 'EST1'),

-- BD2 requiere BD1
('BD2', 'BD1'),

-- SO2 requiere SO1 y RED1
('SO2', 'SO1'),
('SO2', 'RED1');

-- =========================
-- PLANES
-- =========================
INSERT INTO planes (clave, carrera_clave, materia_clave) VALUES
-- ISC
('P01','ISC', 'MAT1'), ('P01','ISC', 'PROG1'), ('P01','ISC', 'LOG1'),
('P01','ISC', 'MAT2'), ('P01','ISC', 'PROG2'), ('P01','ISC', 'EST1'),
('P01','ISC', 'MAT3'), ('P01','ISC', 'ED1'), ('P01','ISC', 'BD1'),
('P01','ISC', 'SO1'), ('P01','ISC', 'RED1'),
('P01','ISC', 'BD2'), ('P01','ISC', 'SO2'),

-- IIA
('P02','IIA', 'MAT1'), ('P02','IIA', 'PROG1'), ('P02','IIA', 'LOG1'),
('P02','IIA', 'MAT2'), ('P02','IIA', 'PROG2'), ('P02','IIA', 'EST1'),
('P02','IIA', 'MAT3'), ('P02','IIA', 'ED1'),
('P02','IIA', 'IA1'), ('P02','IIA', 'IA2'),

-- IMEC
('P03','IMEC', 'MAT1'), ('P03','IMEC', 'MAT2'), ('P03','IMEC', 'MAT3'),
('P03','IMEC', 'EST1');
