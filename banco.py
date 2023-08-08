import sqlite3
from time import sleep

print("Entrando no arquivo de execução do banco")

try:
    conn = sqlite3.connect('aplication.sqlite3')
    for indice in range(10):
        print("*")
        sleep(0.5)
    print("Você está conectado!")

except Exception:
    print("Sua conexão falhou. Verifique novamente.")

if conn is not None:
    print("Conexão estabelecida...")

    cursor = conn.cursor()

    try:
        cursor.execute('CREATE TABLE pessoa(id INTEGER PRIMARY KEY, nome VARCHAR(15) NOT NULL, idade INTEGER NOT NULL, altura VARCHAR(4) NOT NULL);')
        print("Sua tabela pessoa foi criada.")

    except Exception:
        print("Sua execução falhou. Verifique a sintax da tabela pessoa.")

    try:
        cursor.execute('CREATE TABLE usuarios(nome VARCHAR(15), nickname VARCHAR(15) PRIMARY KEY NOT NULL, senha VARCHAR(15) NOT NULL);')
        print("Sua tabela usuarios foi criada.")

    except Exception:
        print("Sua execução falhou. Verifique a sintax da tabela usuarios.")

    conn.commit()
    cursor.close()
    conn.close()
