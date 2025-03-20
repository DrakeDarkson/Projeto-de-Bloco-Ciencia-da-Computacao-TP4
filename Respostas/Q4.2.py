import socket

def cliente_tcp():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.connect(('localhost', 12345))

    mensagem = "Olá, servidor!"
    cliente.send(mensagem.encode())

    resposta = cliente.recv(1024).decode()
    print("Resposta do servidor:", resposta)

    cliente.close()

cliente_tcp()
