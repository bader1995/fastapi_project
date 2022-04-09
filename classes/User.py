import datetime
import mysql.connector
from classes.Conn import Conn


class User():

    def getAllUsers():
        myCon = Conn.connect()
        mycursor = myCon.cursor()
        mycursor.execute("SELECT * FROM fastapi.users")
        return mycursor.fetchall()

    def addUser(user):
        myCon = Conn.connect()
        mycursor = myCon.cursor()
        mycursor.execute("INSERT INTO fastapi.users (first_name, last_name, email, created_at) VALUES (%s, %s, %s, %s)", (user.first_name, user.last_name, user.email, user.created_at))
        return myCon.commit()

    def deleteUser(id):
        myCon = Conn.connect()
        mycursor = myCon.cursor()
        mycursor.execute("DELETE FROM fastapi.users WHERE id = %s", (id))
        return mycursor.commit()