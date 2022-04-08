from operator import truediv
import os
import sqlite3
import smtplib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def update_categoria(Id):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "UPDATE Categoria SET nombre=? WHERE Id=?"
    sql2=cursor_db.execute(sql, (Id,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False
