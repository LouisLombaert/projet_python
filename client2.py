import socket


def function_client():
    ip="127.0.0.1"                                              #IP local ou IP server si distant
    port=64000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Créé un objet socket
    s.connect((ip, port))  # Connecter au socket

    msg = ''

    while msg != 'Bye':
        """tant que le client n'envoi pas 'Bye', la conversation continue"""
        msg = input('Votre message : ')
        s.send(msg.encode())

        rep = s.recv(1024)  # En attente de réception
        rep = rep.decode()
        print("                                                 Nathan 2 : '{}'".format(rep))


if __name__ == "__main__":
    """appel de la fonction function_client"""
    function_client()
