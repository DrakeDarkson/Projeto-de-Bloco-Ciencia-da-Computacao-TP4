import socket

def servidor_udp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(("localhost", 12345))
    print("Servidor UDP aguardando mensagens...")

    while True:
        mensagem, endereco = servidor.recvfrom(1024)
        print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")
        servidor.sendto(b"ack", endereco)

servidor_udp()
