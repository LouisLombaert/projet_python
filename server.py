import socket

myIP="127.0.0.1"                                        #IP local ou IP server si distant
myPort=64000
bufferSize=1024


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Créé un objet socket
s.bind((myIP, myPort))                                  #Initialisation socket
s.listen(1)                                             #Ecoute une connexion
(cl, adress) = s.accept()                               #Récupere coordonée client et attibution variable

rep=''

while(rep != 'Bye'):
    msg=cl.recv(bufferSize)                             #Récupere le message encodé
    msg=msg.decode()
    print("                                             Nathan 1 : '{}'".format(msg))

    rep=input('Votre réponse : ')
    cl.send(rep.encode())