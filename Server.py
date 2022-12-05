from fastapi import FastAPI
import sqlite3
import random
from fastapi.middleware.cors import CORSMiddleware
from config import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/Restaurant")
def Restaurant():
    restaurantes = []
    enderecos = []
    caminhoBanco = database['caminho']

    banco = sqlite3.connect(caminhoBanco)
    cursor = banco.cursor()

    querySelector = "SELECT * FROM Restaurantes"
    cursor.execute(querySelector)
    retorno = cursor.fetchall()

    for restaurante in retorno:
        local = restaurante[0]
        endereco = restaurante[1]
        restaurantes.append(local)
        enderecos.append(endereco)
    
    valorSorteado = random.randint(0,(len(restaurantes)-1))
    localSelecionado = restaurantes[valorSorteado]
    LinkURL = enderecos[valorSorteado]
    JsonList = {"LocalSelecionado": localSelecionado,"LinkURL": LinkURL}

    return JsonList