## Uma forma de fazer interacao com APIs
## Requisicoes: GET (pegar), POST(lancar), PATCH(modificar), DELETE(deletar)
##* Todas essas requisicoes soh podem ser feitas se forem aprovadas/liberadas*
## OBS: caso o 'print(requisicao)' retorne '200' = Funcionou!!

import requests

##AwesomeAPI
##requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 

##* Imprimir uma informacao
## requisicao = requests.get("https://primeiro-projeto-a0bf3-default-rtdb.firebaseio.com/.json")
## print(requisicao)
## print(requisicao.json())

##* Postar uma informacao
## informacoes = '{"Nome": "Gabriel"}'
## requisicao = requests.post("https://primeiro-projeto-a0bf3-default-rtdb.firebaseio.com/.json", data=informacoes)
## print(requisicao)
## print(requisicao.json())

##* Alterar uma informacao
## informacoes = '{"Nome": "Gabriel", "Sobrenome": "Pedroso", "Idade": "24"}'
## requisicao = requests.path("https://primeiro-projeto-a0bf3-default-rtdb.firebaseio.com/-O1C3fPwjK_d0tcjkc62.json", data=informacoes)
## print(requisicao.json())

##* Deletar uma informacao
requisicao = requests.delete("https://primeiro-projeto-a0bf3-default-rtdb.firebaseio.com/-O1C3fPwjK_d0tcjkc62/-O1C57KEnAdjTdmhRXF0.json")