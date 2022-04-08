import os
import sqlite3
import smtplib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def delete_categoria(Id):
    id=int(Id)
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  Categoria WHERE Id=?"
    sql2=cursor_db.execute(sql, (id,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False


def delete_usuario(id):
    id=int(id)
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  Usuarios WHERE Id=?"
    sql2=cursor_db.execute(sql, (id,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False



def delete_producto(Id):
    id=int(Id)
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  producto WHERE Id=?"
    sql2=cursor_db.execute(sql, (id,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False


def delete_proveedor(Id):
    id=int(Id)
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  proveedor WHERE Id=?"
    sql2=cursor_db.execute(sql, (id,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False


def delete(correo):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "DELETE FROM  usuarios WHERE correo=?"
    cursor_db.execute(sql, (correo,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql:
        return "Datos eliminados correctamente"
    else:
        return "Los datos no han sido eliminados, el correo no coincide"
