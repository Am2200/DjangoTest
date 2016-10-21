import psycopg2

class DB:

    dbName = ""
    dbUser = ""
    dbPassword = ""

    dbConnetion = 0


    def __init__(self, name, user, password):
        self.dbName = name
        self.dbUser = user
        self.dbPassword = password

