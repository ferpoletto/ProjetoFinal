from app.models.bd import Connection

class Validacoes:
    def __init__(self):
        self.dominio = "http://127.0.0.1:5000/urls/"

    def short_url_existe(self, codigo):
        self.short_url = self.dominio+codigo
        self.bd = Connection()
        self.query = ("SELECT * FROM links WHERE shorturl = '{0}'".format(self.short_url))
        self.result = self.bd.findOne(self.query)
        if not self.result:
            return False
        return True

    def id_existe(self, id):
        self.bd = Connection()
        self.query = ("SELECT * FROM links WHERE id = {0}".format(id))
        self.result = self.bd.findOne(self.query)
        if not self.result:
            return False
        return True

    def http_existe_na_url(self,URL):
        if URL[:7] == 'http://' or URL[:8] == 'https://':
            return URL
        return 'http://'+URL

    def existem_dados(self, id=None):
        self.bd = Connection()

        if id:
            self.query = f"SELECT count(id) FROM links WHERE usuario_id = {id}"
        else:
            self.query = "SELECT * FROM links"

        self.results = self.bd.findOne(self.query)
        if self.results and self.results[0][0] !=0:
            return True
        return False

    def user_existe(self, user=None, id=None):
        self.bd = Connection()
        if user:
            self.query = ("SELECT count(id_usuario) FROM users where usuario = '{0}'".format(user))
        if id:
            self.query = ("SELECT count(id_usuario) FROM users where id_usuario = {0}".format(id))
        self.result = self.bd.findOne(self.query)
        if self.result[0][0] == 1:
            return True
        return False

    def existe_url_do_usuario(self, id):
        self.bd = Connection()
        self.results = self.bd.findOne("SELECT count(id) FROM links WHERE id_usuario = {0}".format(id))
        if self.results:
            return True
        return False
