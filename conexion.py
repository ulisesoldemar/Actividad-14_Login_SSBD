import mysql.connector

bd = mysql.connector.connect(
    user='ulises', password='passinseguraxd',
    database='cinemapp')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"
    usuarios = []
    cursor.execute(consulta)
    for row in cursor.fetchall():
        usuario = {
            'id': row[0],
            'correo': row[1],
            'contraseña': row[2]
        }
        usuarios.append(usuario)
    return usuarios

def existe_usuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    return cursor.fetchone()[0] == 1

import hashlib
def crear_usuario(correo, contra):
    if existe_usuario(correo):
        return False
    else:
        h = hashlib.new('sha256', bytes(contra, 'utf-8'))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario(correo, contraseña) VALUES(%s, %s)"
        cursor.execute(insertar, (correo, h))
        bd.commit()

        return True

def iniciar_sesion(correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND contraseña = %s"
    cursor.execute(query, (correo, h))
    id = cursor.fetchone()
    if id:
        return id[0], True
    else:
        return None, False