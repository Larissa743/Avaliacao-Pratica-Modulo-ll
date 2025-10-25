"""
Avaliação - Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""


import sqlite3

conn= sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nome TEXT NOT NULL, 
               idade INTEGER,
               email TEXT 
               )''')
print('Tabela criada com sucesso!\n')

cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',('Catherine',46,'cate@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',('Sandra',50,'sandra@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',('Sarah',36,'sarah@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',('Helena',52,'helena@gmail.com'))

conn.commit()
print('Dados inseridos com êxito!\n')

print('Lista de alunos cadastrados:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('UPDATE alunos SET email = ? WHERE id = ?',('cateblanket@gmail.com', 1))
conn.commit()
print('Após atualização do email da Catherine:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('DELETE FROM alunos WHERE id= ?',(2,))
conn.commit()
print('Após deletar o id 1:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

conn.close()
