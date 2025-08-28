import sqlite3
from config import DATABASE
con = sqlite3.connect('help.db')
cur = con.cursor()

class DB_Manager:
    def __init__(self, database):
        self.database = database
        