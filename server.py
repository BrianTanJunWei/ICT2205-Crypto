import socket
import threading
import sys

#params
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
BYTE_RECV = 64


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (SERVER, PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# Listen for incoming connections

def handle_client(connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    connected = True
    while connected:
        data = connection.recv(BYTE_RECV)
        print('received {!r}'.format(data))
        if data == DISCONNECT_MESSAGE:
            connected = False
    
    connection.close()



def start():
    try:
        sock.listen(2) #listen to 2 connection, client A and client B
        print('waiting for a connection')
        while True:
            connection, client_address = sock.accept()
            thread = threading.Thread(target=handle_client, args=(connection, client_address))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("Ctrl+C pressed. Closing server socket.")
        sock.close()
        sys.exit(0)


print("[STARTING] server is starting...")
start()







# while True:
#     # Wait for a connection
#     print('waiting for a connection')
#     connection, client_address = sock.accept()
#     try:
#         print('connection from', client_address)
#         # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(16)
#             print('received {!r}'.format(data))
#             if data:
#                 print('sending data back to the client')
#                 connection.sendall(data)
#             else:
#                 print('no data from', client_address)
#             break
#     finally:
#     # Clean up the connection
#         connection.close()