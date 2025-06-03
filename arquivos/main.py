import os 
import pandas as pd 

df_pedidos = pd.read_excel("pedidos.xlsx")
df_produtos = pd.read_excel("produtos.xlsx")
df_financeiro = pd.read_excel("financeiro.xlsx")

df_juntar = pd.concat([df_pedidos, df_produtos, df_financeiro], axis=1)

df_juntar.to_excel("juntar.xlsx", index=False)

df_juntar = pd.read_excel("juntar.xlsx")

df_juntar = df_juntar.drop('Contato do cliente', axis=1)

df_juntar.to_excel("dados_tratados.xlsx", index=False)



print("Arquivo juntar.xlsx criado com sucesso!")




            