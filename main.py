import pandas as pd
import requests

# Busca do endereço pelo cep

cep = "79042170"
cep = cep.replace("-", "").replace(".", "").replace(" ", "")
link = f'https://viacep.com.br/ws/{cep}/json/'
if len(cep) == 8:
    requisicao = requests.get(link)
    print(requisicao)  # valor=200 o site está respondendo
    dic_requisicao = (requisicao.json())
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    logradouro = dic_requisicao['logradouro']
    print(f'uf: {uf}, cidade: {cidade}, bairro: {bairro}, logradouro: {logradouro}')
else:
    print("Cep Invalido")

print("##########################################################################################")
# Busca de cep a partir do endereço

uf = "MS"
cidade = "Campo Grande"
endereco = "Rua Mona Lisa"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(requisicao)

lista_requisicao = requisicao.json()
# imprimir todos os CEPs
#print(lista_requisicao)

# imprime somente o primeiro da lista
dic_logradouro = lista_requisicao[0]
print(f'CEP: {dic_logradouro["cep"]}')

# Para usar com o jupyter(Abre em formato de planilha)
# tabela = pd.DataFrame(lista_requisicao)
# display(tabela)
