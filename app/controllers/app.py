from http import HTTPStatus

from flask import request, jsonify
from werkzeug.utils import redirect

from app.controllers.links import Links
from app.controllers.utils import Utils
from app.controllers.validacoes import Validacoes
from app.controllers.users import *
from app.models.bd import *

from flask import Flask

app = Flask(__name__)

executor = Connection()
executor.executor()

@app.route("/users/<userid>/urls", methods=["POST"])
def encurtarURL(userid):
    data = request.json

    garanta = Validacoes()
    if not garanta.user_existe(id=userid):
        return 'Usuário não existe', HTTPStatus.NOT_FOUND

    short = Links()
    data = short.cadastra_urls(data["URL"], userid)

    utils = Utils()
    data = utils.gera_dict(data)
    return jsonify(data), HTTPStatus.CREATED


@app.route("/urls/<codigo>", methods=["GET"])
def redireciona(codigo):
    garanta = Validacoes()

    if not garanta.short_url_existe(codigo):
        return '', HTTPStatus.NOT_FOUND

    link = Links()
    link.registra_hits(codigo)
    url_original = link.find_url_original(codigo)

    return redirect(url_original[0][0], HTTPStatus.MOVED_PERMANENTLY)


@app.route("/stats/<id>", methods=["GET"])
def stats_id(id):
    garanta = Validacoes()
    if not garanta.id_existe(id):
        return '', HTTPStatus.NOT_FOUND

    url = Links()
    results = url.get_stats_by_id(id)
    utils = Utils()
    results = utils.gera_dict(results)
    return jsonify(results)


#Status gerais de todas URLs cadastradas no sistema.
@app.route("/stats", methods=['GET'])
def stats():
    garanta = Validacoes()
    results = garanta.existem_dados()
    if not results:
        return 'No Data', HTTPStatus.NOT_FOUND

    links = Links()
    stats_geral = links.get_analitcs()
    return jsonify(stats_geral)


#Status das URLS cadastradas por usuário,
#Routa considera o id(primary key) do usuário salvo no banco
@app.route("/users/<userid>/stats", methods=["GET"])
def getUserStats(userid):

    garanta = Validacoes()
    if not garanta.user_existe(id=userid):
        return 'Usuário não existe', HTTPStatus.NOT_FOUND

    if not garanta.existem_dados(userid):
        return 'Não existem dados para esse usuário', HTTPStatus.NOT_FOUND


    links = Links()
    stats_user = links.get_analitcs(id=userid)
    return jsonify(stats_user)


#Deleta uma URL cadastrada
@app.route("/urls/<id>", methods=["DELETE"])
def delete(id):
    garanta = Validacoes()
    results = garanta.id_existe(id)
    if not results:
        return '', HTTPStatus.NOT_FOUND
    link = Links()
    link.delete_url(id)
    return '', HTTPStatus.OK


#Cadastra um usuário na tabela users
@app.route("/users", methods=["POST"])
def cadastrarUser():
    data = request.json

    garanta = Validacoes()
    if garanta.user_existe(user=data['id']):
        return '', HTTPStatus.CONFLICT

    user = Users()
    user.cadastrarUser(data['id'])
    id_pk = user.get_usuario_id(data['id'])
    results = {'id_PK': id_pk[0][0], 'usuario': data['id']}
    return jsonify(results), HTTPStatus.CREATED


#Deleta um usuário e suas URLS cadastradas
@app.route("/users/<id>", methods=['DELETE'])
def deletarUser(id):
    garanta = Validacoes()
    if not garanta.user_existe(id=id):
        return 'User não existe', HTTPStatus.NOT_FOUND

    links = Links()
    if garanta.existe_url_do_usuario(id):
        links.delete_url(id_usuario=id)

    user = Users()
    user.deletarUser(id)

    return '', HTTPStatus.OK
