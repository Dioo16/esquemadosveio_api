from fastapi import FastAPI
from funcoes import numeros_escolhidos, transforma_em_lista_numeros_get, tabela_dos_numeros
import uvicorn
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/retorna-numeros-concurso/{numeros}")
async def get_produtos_vendidos(numeros: str):
    
    lista_numeros = transforma_em_lista_numeros_get(numeros)
    tabela = tabela_dos_numeros(lista_numeros)
    possiveis_numeros = numeros_escolhidos(lista_numeros)
    return possiveis_numeros

@app.get("/tabela_do_esquema/{numeros}")
async def tabela_do_esquema(numeros: str):
    
    lista_numeros = transforma_em_lista_numeros_get(numeros)
    tabela = tabela_dos_numeros(lista_numeros)
    
    return tabela

# if __name__ == '__main__':
#     uvicorn.run(app, port=8090, host='127.0.0.1')
