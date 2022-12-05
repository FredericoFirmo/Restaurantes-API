# Restaurantes-API

Este projeto implementa um método GET para fornecer aleatoriamente um restaurante cadastrado no banco de dados.

## Uvicorn, sqlite3 e FastAPI

Uvicorn é uma implementação de servidor web para python.
sqlite3 é uma biblioteca que implementa um banco de dados SQL.
FastAPI é um framework Web para desenvolvimento de APIs RESTful em Python.

## Instalação de bibliotecas
Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as bibliotecas necessárias.

```bash
pip install uvicorn
pip install db-sqlite3
pip install fastapi
```

## Execução do programa

Rode o arquivo main.py e acesse o link a seguir para o endpoint: http://127.0.0.1/Restaurant

## Resultado esperado:

{
  "LocalSelecionado": "local",
  "LinkURL": "https:linkparaolocal"
}

