from time import sleep
from socket import socket
from threading import Thread


def processar(conexao, opcao):
    sleep(5)
    print("Processando Requisição...")

    ip1 = "127.0.0.1"
    porta1 = "3001"

    ip2 = "127.0.0.1"
    porta2 = "3002"

    verificacao = 1

    if opcao == 'servidor1':
        conexao.sendall(bytes(str(verificacao), "UTF-8"))
        conexao.sendall(bytes(str(ip1), "UTF-8"))
        conexao.sendall(bytes(str(porta1), "UTF-8"))
        print("Informações do Servidor1 enviadas!")

    elif opcao == 'servidor2':
        conexao.sendall(bytes(str(verificacao), "UTF-8"))
        conexao.sendall(bytes(str(ip2), "UTF-8"))
        conexao.sendall(bytes(str(porta2), "UTF-8"))
        print("Informações do Servidor2 enviadas!")

    else:
        verificacao = -1
        conexao.sendall(bytes(str(verificacao), "UTF-8"))
        print("Servidor não encontrado")
        print("Informações enviadas!")

    conexao.close()
    print("Processamento Encerrado!")


def escutar():

    print("Iniciando Servidor Central")
    socket_bind_info = ('127.0.0.1', 3003)
    sck = socket()
    sck.bind(socket_bind_info)
    print("Servidor Central Iniciado!")
    sck.listen()

    while True:
        try:
            conexao, origem = sck.accept()
            print("Nova conexão estabelecida...")
            opcao = conexao.recv(1000).decode("UTF-8")

            processar(conexao, opcao)

        except KeyboardInterrupt:
            conexao.close()
            print("Programa Encerrado!")

if __name__ == '__main__':


    escutar()