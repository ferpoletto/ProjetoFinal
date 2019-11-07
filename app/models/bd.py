import psycopg2

class Connection():

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="postgres",
                host="127.0.0.1",
                port="5432",
                database="links")
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

    def executor(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users '
                            '(id_usuario serial primary key,'
                            'usuario varchar(30) not null unique)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS links '
                            '(id serial primary key,'
                            'hits integer not null,'
                            'url varchar(100) not null,'
                            'shorturl varchar(100) not null unique,'
                            'usuario_id integer not null,'
                            'FOREIGN KEY (usuario_id) '
                            'REFERENCES users(id_usuario))')

