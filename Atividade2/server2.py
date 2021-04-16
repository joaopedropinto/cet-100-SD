from time import sleep
from socket import socket
from threading import Thread


def processar(conexao, vetor , valor, tam):
    print("Processando Requisição...")
    i = 0
    n = len(vetor) - 1
    while i < n:
        if vetor[i] == valor:
            i = i + (tam/2)
            conexao.sendall(bytes(str("Encontrado na posição: ", i), "UTF-8"))
            print("Encontrado na posição: ",i)
            print("Processamento Encerrado!")


        i = i + 1

    conexao.sendall(bytes(str("Não Encontrado!"), "UTF-8"))
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
            vetor = conexao.recv(1000).decode("UTF-8")
            print("Vetor aceito...")
            print(vetor)
            valor = conexao.recv(1000).decode("UTF-8")
            print("Valor a ser buscado aceito...")
            print(valor)
            tam = conexao.recv(1000).decode("UTF-8")
            print("Tamanho do vetor aceito...")
            print(tam)
            processar(conexao, vetor, valor, tam)

            #thread = Thread(target=processar, args=(conexao, vetor, valor, tam ))
            #thread.start()
            #print(f"Thread iniciada - {thread}")

        except KeyboardInterrupt:
            conexao.close()
            print("Programa Encerrado!")


if __name__ == '__main__':
    escutar()