from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config


def connect():

    try:

        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database')

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Persons")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
