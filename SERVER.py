import socket
import random

PORT = 9087
IP = "10.108.33.18"
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    rand = random.randint(0, 9)
    print(clientsocket)
    ip =clientsocket.getpeername()
    ip = ip[0:1]
    ip = str(ip[0])
    ip = ip.replace(".","")
    ip=list(ip)
    suma = 0
    print(rand)
    for i in ip:
        suma += int(i)
    resto = suma % 10
    ganador = str(("FELICIDADES!! Te ha tocado la lotería, el número era:", resto))
    perdedor =str(("MALA SUERTE!! NO te ha tocado la lotería, tu número era:", resto))

    if resto == rand:
        clientsocket.send(str.encode(ganador))
    else:
        clientsocket.send(str.encode(perdedor))

    clientsocket.close()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socketSERVER.py:26SERVER.py:26
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)