import mysql.connector


class Conn:
    def connect():
        mycon = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="fastapi"
        )

        if mycon.is_connected():
            return mycon
        else:
            exit(503)
