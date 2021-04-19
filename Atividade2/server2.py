from time import sleep
from socket import socket
from threading import Thread


def processar(conexao, vetor , valor, tam):
    sleep(5)
    print("Processando Requisição...")
    vetor = vetor[1:-1]

    vetor = vetor.split()
    tam = int(tam)
    i = 0
    n = len(vetor)
    aux = -1


    for i in range(n):
        if vetor[i] == valor:
            aux = i
            break



    if aux == i:

        aux = int(aux)
        aux = int (aux + tam)
        mensagem = "Encontrado na posição: " + str(aux)
        conexao.sendall(bytes(str(mensagem), "UTF-8"))

        print(mensagem)

    else:

        conexao.sendall(bytes(str("Não Encontrado!"), "UTF-8"))
        print("Não Encontrado!")

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