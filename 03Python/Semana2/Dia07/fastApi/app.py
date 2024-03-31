from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Datos de usuarios (simulación)
usuarios = [
    {"id": 1, "nombre": "Juan", "edad": 30},
    {"id": 2, "nombre": "María", "edad": 25},
    {"id": 3, "nombre": "Pedro", "edad": 35}
]

# Ruta para obtener los usuarios
@app.get("/usuarios")
def obtener_usuarios():
    return usuarios

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
