from time import sleep
from socket import socket
from threading import Thread


def processar(conexao, vetor , valor, tam ):
    print("Processando Requisição...")
    sleep(10)
    for i in range(len(vetor) - 1):
        if vetor[i] == valor:
            conexao.sendall('Encontrado na posição: ', i+tam)
            conexao.close()
            print("Processamento Encerrado")

    conexao.send("Não encontrado!")
    conexao.close()
    print("Processamento Encerrado!")


def escutar():
    print("Iniciando Servidor2...")
    socket_bind_info = ('127.0.0.1', 3002)
    sck = socket()
    sck.bind(socket_bind_info)
    sck.listen()
    print("Servidor2 Iniciado!")

    while True:
        try:
            conexao, origem = sck.accept()
            print("Nova conexão estabelecida...")
            sck.accept()
            vetor= sck.recv(1000)
            print("Vetor aceito...")
            sck.accept()
            valor = sck.recv(1000)
            print("Valor a ser buscado aceito...")
            sck.accept()
            tam = sck.recv(1000)
            print("Tamanho do vetor aceito...")
            thread = Thread(target=processar, args=(conexao, vetor, valor, tam ))
            thread.start()
            print(f"Thread iniciada - {thread}")

        except KeyboardInterrupt:
            sck.close()
            print("Programa Encerrado!")


if __name__ == '__main__':
    escutar()