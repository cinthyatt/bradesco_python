import sqlite3
con = sqlite3.connect("nome_do_banco.db")

cur = con.cursor()

cur.execute("CREATE TABLE contato(nome, endereco, telefone)")

