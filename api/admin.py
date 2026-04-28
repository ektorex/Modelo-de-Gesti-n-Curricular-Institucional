from fastapi import FastAPI
from pydantic import BaseModel
from db import get_conn

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# MODELOS
# =========================

class Carrera(BaseModel):
    clave: str
    nombre: str
    fecha_alta: str
    plan_clave: str


class Materia(BaseModel):
    clave: str
    nombre: str
    fecha_alta: str
    semestre: int


class PlanMateria(BaseModel):
    clave: str
    materia_clave: str


class Prereq(BaseModel):
    materia_clave: str
    requisito_clave: str


# =========================
# CARRERAS
# =========================

@app.post("/carreras")
def crear_carrera(c: Carrera):
    conn = get_conn()
    cur = conn.cursor()

    # crear carrera
    cur.execute(
        "INSERT INTO carreras (clave, nombre, fecha_alta) VALUES (%s, %s, %s)",
        (c.clave, c.nombre, c.fecha_alta)
    )

    # asignar plan (actualiza las filas PEND)
    cur.execute(
        "UPDATE planes SET carrera_clave = %s WHERE clave = %s AND carrera_clave = 'PEND'",
        (c.clave, c.plan_clave)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok"}


# =========================
# MATERIAS
# =========================

@app.post("/materias")
def crear_materia(m: Materia):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO materias (clave, nombre, fecha_alta, semestre) VALUES (%s, %s, %s, %s)",
        (m.clave, m.nombre, m.fecha_alta, m.semestre)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok"}


# agregar prerequisito (uno por request)
@app.post("/prerequisitos")
def agregar_prereq(p: Prereq):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO prerequisitos (materia_clave, requisito_clave) VALUES (%s, %s)",
        (p.materia_clave, p.requisito_clave)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok"}


# =========================
# PLANES
# =========================

@app.post("/planes")
def agregar_materia_a_plan(p: PlanMateria):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO planes (clave, carrera_clave, materia_clave) VALUES (%s, 'PEND', %s)",
        (p.clave, p.materia_clave)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok"}


# =========================
# GETs (para selects frontend)
# =========================

@app.get("/materias")
def get_materias():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT clave, nombre FROM materias")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


@app.get("/planes")
def get_planes():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT clave FROM planes")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return data

@app.delete("/materias/{clave}")
def eliminar_materia(clave: str):
    conn = get_conn()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM materias WHERE clave = %s", (clave,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

    return {"status": "ok"}

@app.delete("/planes/{clave}")
def eliminar_plan(clave: str):
    conn = get_conn()
    cur = conn.cursor()

    try:
        # evita borrar si ya está asignado a carrera
        cur.execute("""
            SELECT 1 FROM planes
            WHERE clave = %s AND carrera_clave != 'PEND'
            LIMIT 1
        """, (clave,))

        if cur.fetchone():
            return {"error": "El plan ya está asignado a una carrera"}

        cur.execute("DELETE FROM planes WHERE clave = %s", (clave,))
        conn.commit()

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

    return {"status": "ok"}

@app.delete("/carreras/{clave}")
def eliminar_carrera(clave: str):
    conn = get_conn()
    cur = conn.cursor()

    try:
        # opcional: liberar planes a PEND
        cur.execute("""
            UPDATE planes SET carrera_clave = 'PEND'
            WHERE carrera_clave = %s
        """, (clave,))

        cur.execute("DELETE FROM carreras WHERE clave = %s", (clave,))
        conn.commit()

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

    return {"status": "ok"}

