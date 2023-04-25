# Importando SQL para o Python 
"""
Para integrar fazer os seguintes passos: 

Passo 1: import pyodbc   # comando de integração

Passo 2: Criar uma variavel de conexão 

dados_conexão = (
    "Driver={SQL Server};" 
    "Server={Blaya};" 
    "DataBase=PythonSQL;"
)

Passo 3: Criar uma variavel de conexão dos dados

Passo 4: Print 

Passo 5: executar 

Passo 6: Criar um cursor - "New Query"

Passo 7 : Copiar o codigo do SQL e fazer um comando com aspas triplas

INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Lucas Blaya', 'IPHONE', '24/06/2023', 8.000, 1)

Passo 8: executando o cursor (comando)

Passo 9: Commit para inserir mais dados

"""
#import pyodbc  
import pyodbc

#Criar uma variavel para receber dados
dados_conexao = (
    "Driver={SQL Server};" 
    "Server={Blaya};" 
    "DataBase=PythonSQL;"
)

# Criar uma variavel de conexão 
conexao = pyodbc.connect(dados_conexao)

#Print 
print("Conexão Bem sucedida")

#Criar um cursor - "New Query" da conexao
cursor = conexao.cursor(

)

# Fazendo um comando com 3 aspas
comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Lucas Blaya', 'IPHONE', '24/06/2023', 8.000, 1)"""


# Executando o cursor (comando)
cursor.execute(comando)

# Commit no cursor 
cursor.commit()