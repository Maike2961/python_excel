import pandas as pd
from twilio.rest import Client
#from teste import sid, token, from_tel
from dotenv import load_dotenv
import os

load_dotenv(override=True)
sid1 = os.getenv("sid")
token1 = os.getenv("token")
from_tel = os.getenv("from_tel")

client = Client(sid1 , token1)
print(sid1)
print(token1)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if(tabela_vendas['Vendas'] > 55000).any():
      vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
      vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
      print(f"No mês {mes}, O vendedor: {vendedor}, vendeu o total de: {vendas}, batendo a meta")
      message = client.messages.create(to=from_tel,from_="+15855427360", body= f"No mês {mes}, O vendedor: {vendedor}, vendeu o total de: {vendas}, batendo a meta")
     
