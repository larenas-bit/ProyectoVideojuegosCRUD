import os

try:
    import mysql.connector
    from mysql.connector import Error as MySQLError
except ModuleNotFoundError as exc:
    raise RuntimeError(
        "No se encontró mysql-connector-python. Instálalo con: pip install mysql-connector-python"
    ) from exc


def conectar():
    config = {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "1234"),
        "database": os.getenv("MYSQL_DATABASE", "videojuegos_db"),
    }

    try:
        return mysql.connector.connect(**config)
    except MySQLError as exc:
        raise RuntimeError(
            f"No se pudo conectar a MySQL en {config['host']}:{config['port']} con el usuario {config['user']}: {exc}"
        ) from exc