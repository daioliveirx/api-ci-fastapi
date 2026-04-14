from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API funcionando!"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}

class Usuario(BaseModel):
    nome: str
    idade: int

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    return {
        "mensagem": "Usuário criado com sucesso",
        "usuario": usuario
    }
