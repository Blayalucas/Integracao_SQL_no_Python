# Criar um SQL   "PythonSQL"   

"""

Passo 6: apagar o create database PythonSQL
Passo 7: digitar Use PythonSQL
Passo 8: Criar uma tabela embaixo 
Exemplo: " informação" dentro de tupas
CREATE TABLE Vendas(
    id_venda int,
    cliente varchar(50),  # varchar == caracteres
    produto varchar(50),  # varchar == caracteres
    data_venda date,
    preco decimal(3,2),
    quantidade int,
    )
Passo 9: Clicar no play (execute)
Passo 10 : Apagar tudo e digitar  # "As mesma informações da Table "

INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Lucas Blaya', 'IPHONE', '24/06/2023', 8.000, 1)

Passo 11: Clicar no play (execute)
Passo 12: Abrir uma Nova Consulta (New Query)
Passo 13: Digitar 
Use PythonSQL
select * from Vendas

OBS: Para criar uma outra consultar basta "executar" e "executar" 
"""