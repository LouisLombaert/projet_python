import socket


def function_server():
    """création d'une conversation entre le client et le serveur"""
    myIP="127.0.0.1"                                        #IP local ou IP server si distant
    myPort=64000
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Créé un objet socket
    s.bind((my_ip, my_port))  # Initialisation socket
    s.listen(1)  # Ecoute une connexion
    (cl, adress) = s.accept()  # Récupere coordonée client et attibution variable

    rep = ''

    while rep != 'Bye':
        """tant que la réponse du client n'est pas 'Bye', continuer la conversation"""
        msg = cl.recv(buffer_size)  # Récupere le message encodé
        msg = msg.decode()
        print("                                             Nathan 1 : '{}'".format(msg))

        rep = input('Votre réponse : ')
        cl.send(rep.encode())


if __name__ == "__main__":
    """appel de la fonction function_server"""
    function_server()
