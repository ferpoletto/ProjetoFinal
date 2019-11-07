import psycopg2

class Connection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="postgres",
                host="127.0.0.1",
                port="5432",
                database="projetoFinal")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except:
            print('Falha na conexão com o banco')

    def executarSQL(self, query):
        try:
            self.cursor.execute(query)
        except:
            print('Falha ao executarSQL')

    def findOne(self, query):
        try:
            result = self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except:
            return ('Falha ao executarSQLRetorno')


