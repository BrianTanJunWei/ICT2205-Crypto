import socket
import sys

def send(msg):
        # Send data
        message = msg
        print('sending {!r}'.format(message))
        sock.sendall(message.encode())

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
    # send("Authenticated")
    connect = True
    while connect:
        print("Welcome To Coin Flip!")
        print("Heads for rolls <= 50")
        print("Tails for rolls > 50\n")

        print("Enter '1' To Start New Game")
        print("Enter '2' To Verify Roll")
        print("Enter '3' To Change Client Seed")
        print("Enter '4' To End The Program")
        #print("This is changeSeed: " + changeSeed)
        
        message = input()
        if message == "4":
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
    send(DISCONNECT_MESSAGE)
    sock.close()
    sys.exit(0)

    
    
