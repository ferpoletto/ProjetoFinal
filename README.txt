Encurtador de URL's 

Foi desenvolvida uma api stateless persistindo os dados no banco de dados relacional Postgres. 

O banco de dados possui 2 tabelas: 
users(id_usuario, usuario);
links(id, hits, url, shorturl, usuario_id);

Se relacionam através da chave estrangeira 'usuario_id' que se refere a chave primaria 'id_usuario' da tabela users. 

DEPLOY:
1 - Baixar o projeto
2 - Abrir o terminal na pasta do projeto
3 - Executar o arquivo install.sh digitando no terminal (./install.sh)
4 - Permitir as instalações das dependências quando solicitado. 
5 - Executar o arquivo start.sh digitando no terminal (./start.sh)

Ao final do deploy, a aplicação estará rodando.



CADASTRAR USUÁRIO:
POST - 127.0.0.1:500/users
Body: {"id":"<nomeUsuario>"}

A aplicação retornará um response 201 -Create. Caso o nome informado já tenha sido cadastrado, retorna um 409 - Conflict. 
Quando o cadastro ocorre com sucesso, no response haverá o id do novo usuário cadastrado (chave primária, que será utilizada nas demais rotas)



EXCLUIR USUÁRIO:
DELETE - 127.0.0.1:500/users/<id>

Ao informar um id que existe no banco, a aplicação retornará um status 200 - OK, excluindo o usuário e todas as URL cadastradas no banco na tabela links. Caso não exista, retorna um 404 - Not found.



CADASTRAR URL:
POST - 127.0.0.1:5000/users/<userid>/urls
Body: {"URL":"<urlOriginal>"}

A aplicação irá um status 201 - Create. Caso seja informado na rota algum id de usuário que não exista, retornará um 404 - Not Found.
No respose haverá as informações do cadastro da URL juntamente com a shortURL.



REDIRECT:
GET - 127.0.0.1:5000/urls/<codigo>

Após o cadastro da URL na etapa anterior, é possível pegar a shortUrl e enviar uma requição usando o método GET. A aplicação então irá redirecionar para a url original com um status 301 - Moved Permanently. Caso seja informado um código que não exista no banco, o sistema retorna um status 404 - not found. 



DELETAR URL CADASTRADA:
DELETE - 127.0.0.1:5000/urls/<id>

A aplicação irá deletar a URL da tabela links. Caso o ID informado na rota não exista, retorna um 404 -not found. Caso exista, retorna status 200 - OK.



STATUS GERAIS DO SISTEMA:
GET - 127.0.0.1:5000/stats

Retorna a quantidade de hits totais de todas as URLs, quantidade de URLs cadastradas e as 10 URLs com maior número de hits por ordem decrescente. Caso não haja dados no banco, retorna um 404 - Not found.



STATUS POR USUÁRIO:
GET - 127.0.0.1:5000/users/<userid>/stats

Caso o id (chave primaria do usuário cadastrado) não exista ou não possua dados na tabela links, retorna um 404 - Not found. Caso haja, retorna as informações referentes ao respectivo usuário. 



STATUS POR URL
GET - 127.0.0.1:5000/stats/<id>

Caso não haja dados cadastrado na tabela links para o ID informado (chave primária da tabela links), o sistema retorna um 404 - not found. Caso haja dados, retornará as informações da respectiva URL. 
