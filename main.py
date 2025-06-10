import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from datetime import datetime, timedelta

# ler as 3 planilhas 
df_pedidos = pd.read_excel("pedidos_atual.xlsx")
df_produtos = pd.read_excel("produtos.xlsx")
df_financeiro = pd.read_excel("financeiro.xlsx")
# agrupar as 3 planilha em uma só 
df_juntar = pd.concat([df_pedidos, df_produtos, df_financeiro], axis=1)
# excluindo uma coluna na planilha 
df_juntar = df_juntar.drop('Contato do cliente', axis=1)

# gerando outra planilha com os dados tratados 
df_juntar.to_excel("dados_tratados.xlsx", index=False)

print("Arquivo criado com sucesso!")




            