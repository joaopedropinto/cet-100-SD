from socket import socket
import random
import numpy




def requisicao(vet, val):
    sck1 = socket()
    sck2 = socket()

    array1, array2 = numpy.array_split(vet, 2)
    print(array1)
    print(array2)

    server_info1 = ('127.0.0.1', 3001)
    sck1.connect(server_info1)
    print("Conexao com o servidor1 foi aceita!")

    sck1.sendall(bytes(str(array1), "UTF-8"))

    sck1.sendall(bytes(str(val), "UTF-8"))

    server_info2 = ('127.0.0.1', 3002)
    sck2.connect(server_info2)
    print("Conexao com o servidor2 foi aceita!")

    sck2.sendall(bytes(str(array2), "UTF-8"))
    sck2.sendall(bytes(str(val), "UTF-8"))
    sck2.sendall(bytes(str(tam), "UTF-8"))

    print("Aguardando dados servidor1...")
    dados_recebidos1 = sck1.recv(1000).decode("UTF-8")

    print("Aguardando dados servidor2...")
    dados_recebidos2 = sck2.recv(1000).decode("UTF-8")

    print(f"Dado recebido do servidor1 {dados_recebidos1}")
    sck1.close()

    print(f"Dado recebido do servidor2 {dados_recebidos2}")
    sck2.close()


if __name__ == '__main__':
    tam = int(input('Insira o tamanho do vetor desejado: '))

    vet = numpy.random.randint(1, 100, (tam))
    print(vet)

    val = int(input('Insira o valor a ser buscado no vetor: '))
    requisicao(vet, val)