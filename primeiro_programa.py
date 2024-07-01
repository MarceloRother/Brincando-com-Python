import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


## Iniciando a Interface
janela = Tk()
## Mudando o titulo da pagina
janela.title("Cotacao Atual das Moedas")
## Mudando geometria da janela
##janela.geometry("400x400")

## Elemento de texto na pagina
texto_orientacao = Label(janela, text="Clique no botao para ver a cotacao das moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

## Botao para executar funcao
botao = Button(janela, text="Buscar cotacoes Dolar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

## Elemento de texto dinamico
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()