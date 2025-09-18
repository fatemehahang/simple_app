import sqlite3

def create_table():
    connection = sqlite3.connect('data_access/mft_db.db')
    cursor = connection.cursor()
    cursor.execute("create table users  (id integer primary key autoincrement, username text, password text, nickname text, locked boolean)")
    connection.commit()
    connection.close()

def save_user():
    connection = sqlite3.connect('data_access/mft_db.db')
    cursor = connection.cursor()
    cursor.execute("insert into users (username, password, nickname, locked) values (?,?,?,?)", [usernam, password, nickname, locked])
    connection.commit()
    connection.close()