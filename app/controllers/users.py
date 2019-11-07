from app.models.bd import Connection


class Users:

    def cadastrarUser(self, id):
        try:
            self.bd = Connection()
            self.bd.executarSQL("INSERT INTO users (usuario) VALUES ('{0}')".format(id))
        except:
            print('Erro ao cadastrar usuario')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def deletarUser(self, id_usuario):
        try:
            self.bd = Connection()
            self.bd.executarSQL("DELETE FROM users WHERE id_usuario = {0}".format(id_usuario))
        except:
            print('Erro ao cadastrar usuario')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()


    def get_usuario_id(self, nome):
        try:
            self.bd = Connection()
            return self.bd.findOne("SELECT id_usuario FROM users WHERE usuario = '{0}'".format(nome))

        except:
            print('Erro no GET usuario by ID')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()
