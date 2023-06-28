import os
import sqlite3
from Camera import coletarimagens




def criardb():
    connect = sqlite3.connect('base.db')
    cursor = connect.cursor()

    #create table
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255))')

    connect.commit()
    cursor.close()
    connect.close()

def adduser():
    username = input(f'Digite um nome de usuário: ')
    connect = sqlite3.connect('base.db')
    cursor = connect.cursor()
    cursor.execute('''INSERT INTO users(name) VALUES (?)''', (username,))
    connect.commit()
    cursor.close()
    connect.close()
    os.makedirs('Fotos/' + username) #Diretorio para receber fotos do usuario
    coletarimagens(username)

criardb()

