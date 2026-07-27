from conexion import conectar

def agregar_videojuego(titulo, genero, clasificacion, plataforma):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO Videojuegos(Titulo,Genero,Clasificacion,Plataforma)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(sql,(titulo,genero,clasificacion,plataforma))

    conexion.commit()

    cursor.close()
    conexion.close()


def mostrar_videojuegos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Videojuegos")

    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return datos


def eliminar_videojuego(id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM Videojuegos WHERE ID=%s",
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_videojuego(id,titulo,genero,clasificacion,plataforma):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    UPDATE Videojuegos
    SET
    Titulo=%s,
    Genero=%s,
    Clasificacion=%s,
    Plataforma=%s
    WHERE ID=%s
    """

    cursor.execute(sql,
    (
        titulo,
        genero,
        clasificacion,
        plataforma,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()

def buscar_videojuego(titulo):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    SELECT * FROM Videojuegos
    WHERE Titulo LIKE %s
    """

    cursor.execute(sql, ("%" + titulo + "%",))

    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return datos