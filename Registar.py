import os
import sqlite3
import smtplib
from Enviar import enviarCorreo


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def registrar(nombre, apellido, correo, clave, rol):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO usuarios (Nombre,Apellido,Correo,Clave,Rol) VALUES (?,?,?,?,?)"
    #ejecuta la consulta
    sql2=cursor_db.execute(sql, (nombre,apellido,correo,clave,rol,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        enviarCorreo(correo,nombre,rol)
        return True
    else:
        return False


def producto(nombre, descripcion, cantidad, precio_compra, precio_venta, categoria , proveedor):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO producto (nombre,descripcion,cantidad,precio_compra,precio_venta,Categoria, Proveedor) VALUES (?,?,?,?,?,?,?)"
    #ejecuta la consulta
    sql2=cursor_db.execute(sql, (nombre,descripcion ,cantidad,precio_compra,precio_venta,categoria,proveedor,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False


def categoria(nombre):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO Categoria (nombre) VALUES (?)"
    #ejecuta la consulta
    sql2=cursor_db.execute(sql, (nombre,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False


def proveedor(nombre, telefono, direccion):
    #se conecta a la base de datos
    con_bd = sqlite3.connect('codeina.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "INSERT INTO proveedor (nombre,telefono,direccion) VALUES (?,?,?)"
    #ejecuta la consulta
    sql2=cursor_db.execute(sql, (nombre,telefono ,direccion,))
    con_bd.commit()
    #cierre del cursor
    cursor_db.close()
    if sql2:
        return True
    else:
        return False