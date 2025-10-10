import requests
import sqlite3
from datetime import datetime

# Sua chave pessoal do HG Brasil (substitua aqui)
API_KEY = "SUA_CHAVE_AQUI"

# URL da API
url = f"https://api.hgbrasil.com/finance?format=json-cors&key={API_KEY}"

# Fazendo a requisição
response = requests.get(url)
data = response.json()

# Pegando as cotações
dolar = data["results"]["currencies"]["USD"]["buy"]
euro = data["results"]["currencies"]["EUR"]["buy"]

print(f"Cotação do Dólar: R$ {dolar}")
print(f"Cotação do Euro: R$ {euro}")

# Conectando ao banco de dados SQLite
conn = sqlite3.connect("bdcotacoes.db")
cursor = conn.cursor()

# Criando a tabela (se não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS moedas (
    data TEXT,
    dolar REAL,
    euro REAL
)
""")

# Inserindo os dados com data e hora atual
data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO moedas (data, dolar, euro) VALUES (?, ?, ?)",
               (data_atual, dolar, euro))

conn.commit()
conn.close()

print("Dados salvos no banco de dados com sucesso!")
