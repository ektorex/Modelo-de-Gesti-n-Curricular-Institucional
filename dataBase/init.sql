-- =========================
-- TABLA: carreras
-- =========================
CREATE TABLE carreras (
    clave VARCHAR(10) PRIMARY KEY,
    nombre TEXT NOT NULL,
    fecha_alta DATE NOT NULL,
    fecha_baja DATE
);

-- =========================
-- TABLA: materias
-- =========================
CREATE TABLE materias (
    clave VARCHAR(10) PRIMARY KEY,
    nombre TEXT NOT NULL,
    fecha_alta DATE NOT NULL,
    fecha_baja DATE,
    semestre INT NOT NULL
);

-- =========================
-- TABLA: prerequisitos
-- (materia -> requiere -> otra materia)
-- =========================
CREATE TABLE prerequisitos (
    materia_clave VARCHAR(10) NOT NULL,
    requisito_clave VARCHAR(10) NOT NULL,

    PRIMARY KEY (materia_clave, requisito_clave),

    CONSTRAINT fk_materia
        FOREIGN KEY (materia_clave)
        REFERENCES materias(clave)
        ON DELETE CASCADE,

    CONSTRAINT fk_requisito
        FOREIGN KEY (requisito_clave)
        REFERENCES materias(clave)
        ON DELETE RESTRICT
);

-- =========================
-- TABLA: planes
-- =========================
CREATE TABLE planes (
    clave VARCHAR(10) NOT NULL,
    carrera_clave VARCHAR(10) NOT NULL,
    materia_clave VARCHAR(10) NOT NULL,

    PRIMARY KEY (clave, carrera_clave, materia_clave),

    FOREIGN KEY (carrera_clave) REFERENCES carreras(clave),

    CONSTRAINT fk_carrera
        FOREIGN KEY (carrera_clave)
        REFERENCES carreras(clave)
        ON DELETE CASCADE,


    CONSTRAINT fk_materia
        FOREIGN KEY (materia_clave)
        REFERENCES materias(clave)
        ON DELETE RESTRICT

);
