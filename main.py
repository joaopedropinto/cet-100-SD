import json
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<p>Página inicial da plataforma de jogos</p>' \
           '<p>Acesse /jogo1 para Quebra-cabeça</p>' \
           '<p>Acesse /jogo2 para Xadrez</p>' \
           '<p>Acesse /jogo3 para Campo minado</p>' \
           '<p>Acesse /usuarios para listar usuários presentes</p>' \
           '<p>Acesse /usuarios/(nº id) para listar informações de determinado usuário</p>' \
           '<p>Acesse /usuarios/(nº id)/historico para listar histórico de determinado usuário</p>'



@app.route('/jogo1')
def jogo1():
    return 'Quebra-cabeça'


@app.route('/jogo2')
def jogo2():
    return 'Xadrez'


@app.route('/jogo3')
def jogo3():
    return 'Campo minado'

@app.route('/usuarios')
def usuarios():
    return json.dumps(['Player1', 'Player2', 'Player3', 'Player4'])

@app.route('/usuarios/<id>')
def detalhes_do_usuario(id):
    return f'Detalhes do Player{id}'

@app.route('/usuarios/<id>/historico')
def hello(id):
    return f'<a href="#">Histórico do Player{id}</a>'


if __name__ == '__main__':
    app.run()