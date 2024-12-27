import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

my_sql_config = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_DATABASE"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT", 3306)
}

def executar(instrucao):
    try:
        conexao = mysql.connector.connect(**my_sql_config)
        if conexao.is_connected():
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(instrucao)
            resultados = cursor.fetchall()
            conexao.commit()
            print(resultados)
            return resultados
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        raise erro
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
