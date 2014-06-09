#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('producto.db')
    con.row_factory = sqlite3.Row
    return con

def obtener(filtro):
    # obtiene la lista de productos segun filtro de marcas
    # 0 es para cuando no hay marca en especifico y se muestran todos los productos
    if filtro == "0":
        con = conectar()
        c = con.cursor()
        query = "SELECT * FROM  producto"
        resultado = c.execute(query)
        producto = resultado.fetchall()
        con.close()
        return producto
    else:
        con = conectar()
        c = con.cursor()
        query = "SELECT * FROM producto WHERE fk_id_marca=" + filtro
        resultado = c.execute(query)
        producto = resultado.fetchall()
        con.close()
        return producto

def insertar(cod, nombre, desc, col, prec, fk):
    #se inserta nuevo producto a la base de datos
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """INSERT INTO Producto (codigo, nombre, descripcion, color,
    precio, fk_id_marca)
    VALUES (?, ?, ?, ?, ?, ?)"""
    valores = [cod, nombre, desc, col, prec, fk]
    try:
        c.execute(query, valores)
        conn.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    conn.close()
    return exito


def eliminar(cod):
    #con este metodo se eliminan productos de la base de datos
    exito = False
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """DELETE from Producto WHERE codigo = ?"""

    try:
        exito = True
        c.execute(query, [cod])
        conn.commit()
    except qlite3.Error as e:
        exito = False
        print "Error", e.args[0]
    conn.close()
    return exito


def consultar_nombre(name):
    #consultar por un producto segun nombre o productos que contengan
    #la palabra buscada
    conn = sqlite3.connect("producto.db")
    c = conn.cursor()
    query = """SELECT * FROM Producto WHERE nombre LIKE '%"""+name+"""%'"""
    r = (c.execute(query).fetchall())
    if r == None:
        r="Elemento no encontrado"
    return r