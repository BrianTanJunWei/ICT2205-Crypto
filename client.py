import socket
import sys

#params
SERVER = "192.168.1.9" #change according to the localhost ip address
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = (SERVER,PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    def send(msg):
        # Send data
        message = msg
        print('sending {!r}'.format(message))
        
        sock.sendall(message.encode())
    
    connect = True
    while connect:
        message = input()
        if message == "!END":
            connect = False
            send(DISCONNECT_MESSAGE)
        send(message)
    
    print('closing socket')
    sock.close()

    # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print('received {!r}'.format(data))
except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing client socket.")
    sock.close()
    sys.exit(0)

    
    
