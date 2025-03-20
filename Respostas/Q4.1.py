import socket

def servidor_tcp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind(('localhost', 12345))

    servidor.listen(1)
    print("Servidor aguardando conexão...")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Conexão estabelecida com {endereco}")

        mensagem = "Bem-vindo ao servidor TCP!"
        cliente.send(mensagem.encode())

        cliente.close()

servidor_tcp()
