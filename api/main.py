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


class Materia(BaseModel):
    clave: str
    nombre: str
    fecha_alta: str
    semestre: int


# =========================
# ENDPOINTS
# =========================



# Obtener carreras
@app.get("/carreras")
def obtener_carreras():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("select * from carreras where clave != 'PEND'")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

# obtener Materias 
@app.get("/materias")
def obtener_carreras():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM materias")
    rows = cur.fetchall()

    cur.close()
    conn.close()
 
    return rows



# Obtener plan por carrera
@app.get("/planes/{carrera}")
def obtener_plan(carrera: str):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT m.clave, m.nombre, m.semestre
        FROM planes p
        JOIN materias m ON p.materia_clave = m.clave
        WHERE p.carrera_clave = %s
        ORDER BY m.semestre
    """, (carrera,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


# Obtener detalles de materia
@app.get("/materias/{clave}")
def detalle_materia(clave: str):
    conn = get_conn()
    cur = conn.cursor()

    # materia
    cur.execute("""
        SELECT clave, nombre, semestre
        FROM materias
        WHERE clave = %s
    """, (clave,))
    materia = cur.fetchone()

    # prerequisitos
    cur.execute("""
        SELECT requisito_clave
        FROM prerequisitos
        WHERE materia_clave = %s
    """, (clave,))
    reqs = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "materia": materia,
        "requisitos": [r[0] for r in reqs]
    }


