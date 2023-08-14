# importei o mysql
import mysql.connector

# definindo as variaveis
nome = str(input('Digite o seu nome: '))
email =  str(input('Digite o seu email: '))
idade = int(input('Digite a sua idade: '))

#criando a conexão com o mysql 
db_config = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='primeiro_database'
)

# inserindo dados na table
comando_sql = 'INSERT INTO informacoes_cliente (nome, email, idade) VALUES (%s, %s, %s)'
dados_sql = (nome, email, idade)

# enviando os dados
cursor = db_config.cursor()
cursor.execute(comando_sql, dados_sql)
db_config.commit()

