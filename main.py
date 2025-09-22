#criando e conectando com banco de dados
import sqlite3

#Criar uma conexão com banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criamos um obejto chamado de cursor e vai servir para executar os comandos SQL
cursor = conexao.cursor()


#Criando uma table no banco chamada de "alunos"

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     nome TEXT NOT NULL,
     idade INTEGER,
     curso TEXT          
    )
""")
print ("Table criada!")


#Inserindo um valor no banco de dados

cursor.execute("""
INSERT INTO alunos (nome, idade, curso)          
VALUES (?, ?, ?)           
               
""", 
("Laura", 24, "Engenharia")            
               
               )

lista_alunos = [
    ("Raul", 20, "Direito"),
    ("Kazuki", 22, "Cozinheiro"),
    ("Damas", 33, "Programador")
]

#Executemany permite inserir multiplas linhas

cursor.executemany("""
INSERT INTO alunos (nome, idade, curso)          
VALUES (?, ?, ?)  
               """,
lista_alunos               )


#confirmar as alteraçõesdo banco
conexao.commit()
print("Dados onseridos com sucesso!")