#@ Por Antonio-costa00

from faker import Faker
# import json
import pandas as batata

def gera_dados(num_registros: int):    
    fake = Faker()
    registros = []

    for _ in range(num_registros):
        nome = fake.name()
        nomes = nome.split()
        primeiro_nome = nomes[0]
        sobrenome = nomes[1]
        email = fake.email()
        telefone = fake.phone_number()
        senha = fake.password()

        registros.append({
            "primeiro_nome": primeiro_nome,
            "sobrenome": sobrenome,
            "email": email, 
            "telefone": telefone,
            "senha": senha
        })

    return registros

def dados_para_planilha(dados):
    df = batata.DataFrame(dados)
    df.to_excel("Dados_aleatorios.xlsx", index=False)

registros = gera_dados(40)
dados_para_planilha(dados=registros)

#pip install 
#pip install pandas
#pip install openpyxl