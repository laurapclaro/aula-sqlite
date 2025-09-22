#criando e conectando com banco de dados
import sqlite3

# #Criar uma conexão com banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

# #Criamos um obejto chamado de cursor e vai servir para executar os comandos SQL
cursor = conexao.cursor()


# #Criando uma table no banco chamada de "alunos"----------------------

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      nome TEXT NOT NULL,
#      idade INTEGER,
#      curso TEXT          
#     )
# """)
# print ("Table criada!")


# #Inserindo um valor no banco de dados-------------------------------

# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)          
# VALUES (?, ?, ?)           
               
# """, 
# ("Laura", 24, "Engenharia")            
               
#                )

# lista_alunos = [
#     ("Raul", 20, "Direito"),
#     ("Kazuki", 22, "Cozinheiro"),
#     ("Damas", 33, "Programador")
# ]

# #Executemany permite inserir multiplas linhas----------------------------

# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)          
# VALUES (?, ?, ?)  
#                """,
# lista_alunos               )


# #confirmar as alteraçõesdo banco----------------------
# conexao.commit()
# print("Dados onseridos com sucesso!")


#atualizar dados tabela alunos---------------------
#atualizar o nome de um aluno
#Sempre usar WHERE, senao todos os registros serao alterados


# cursor.execute("""
# UPDATE alunos
# SET nome = ?, curso = ?
# WHERE id = ? 
# """, ("Felipe", "Ads", 2))

# conexao.commit()
# print ("Dados alterados com sucesso!")




#Consultar os dados--------------------------------
#Selecionando todos os alunos
cursor.execute("SELECT * FROM alunos")
#fetchall traz todas as linhas de consulta

for linha in cursor.fetchall():
    print(f"ID {linha[0]} | NOME {linha[1]} | IDADE {linha[2]} | CURSO {linha[3]}")

curso = input("Qual curso você deseja ver os alunos? ")
#Selecionando apenas os alunos do curso computação
cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (curso,))
for linha in cursor.fetchall():
    print(linha)