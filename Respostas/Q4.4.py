import socket

def cliente_udp():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.sendto(b"Mensagem de teste", ("localhost", 12345))
    resposta, _ = cliente.recvfrom(1024)
    print(resposta.decode())

cliente_udp()
