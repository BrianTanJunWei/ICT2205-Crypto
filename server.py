import socket
import threading
import sys
import main
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
    nonce = 0
    changeSeed = "No need change"
    client_seed = "GoingToBeChanged"
    server_seed = "GoingToBeChanged"
    status = True
    while connected:
        data = connection.recv(BYTE_RECV)
        print(data)
        if data.decode().strip() == DISCONNECT_MESSAGE:
            connected = False
            connection.close()
            print(f"[DISCONNECTED] {client_address} disconnected.")
        elif len(data) != 0:
            print("testing")
            if data.decode().strip() == "1":
                print("entered 1")
                nonce = main.get_nonce(nonce, status)[0]
                server_seed = main.generate_server_seed(server_seed)
                client_seed, changeSeed = main.generate_client_seed(client_seed, changeSeed)
                roll, server_seed, client_seed = main.get_roll_and_seeds(nonce, server_seed, client_seed)
                print(f'\nRoll for nonce {nonce} is {roll}')
                status = False
                if roll <= 50:
                    print("The result of the coin flip is heads!\n")
                if roll > 50:
                    print("The result of the coin flip is tails!\n")
    #          Append variables to text file
    #          Need to store client seed, server seed, nonce, roll, result.
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