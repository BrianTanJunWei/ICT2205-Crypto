import socket
import threading
import sys
import time

#params
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
BYTE_RECV = 64
ACK_TEXT = 'text_received'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (SERVER, PORT)
print('starting up on {} port {}'.format(*server_address))
# Listen for incoming connections
sock.bind(server_address)
sock.settimeout(1.0)
sock.listen(2) #listen to 2 connection, client A and client B
print('waiting for a connection')

def handle_client(connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    connected = True
    while connected:
        data = connection.recv(BYTE_RECV)
        print(data)
        if data.decode().strip() == DISCONNECT_MESSAGE:
            connected = False
            connection.close()
            print(f"[DISCONNECTED] {client_address} disconnected.")
        elif len(data) != 0:
            print('received {!r}'.format(data))
            print(data.decode().strip())
    return

try:
    while True:
        try:

            connection, client_address = sock.accept()
            thread = threading.Thread(target=handle_client, args=(connection, client_address), daemon = True)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except socket.timeout:
            # print("Timeout")
            pass

except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing server socket.")
    sock.close()
    sys.exit(0)

print("[STARTING] server is starting...")