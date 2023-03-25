import socket
import threading
import sys
import json
import main
import time
import FileHandler as FH
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
# sock.settimeout(5)
sock.listen(2) #listen to 2 connection, client A and client B
print('waiting for a connection')



def handle_client(connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    connected = True
    status = True
    nonce = 0
    changeSeed = "No need change"
    client_seed = "GoingToBeChanged"
    server_seed = "GoingToBeChanged"
#Open file
    file_name = f"{client_address[0]}_{client_address[1]}.txt"
    with open(file_name, "a") as f:

        while connected:
            data = connection.recv(BYTE_RECV).decode().strip()
            if data == DISCONNECT_MESSAGE:
                connected = False
                connection.close()
                print(f"[DISCONNECTED] {client_address} disconnected.")
                FH.convert_text_to_json(file_name, "Result.json")# having issues
            elif len(data) != 0:
                if data == "1":
                    client_answer = ""
                    server_answer = ""

                    nonce = main.get_nonce(nonce, status)[0]
                    server_seed = main.generate_server_seed(server_seed)
                    client_seed, changeSeed = main.generate_client_seed(client_seed, changeSeed)
                    roll, server_seed, client_seed = main.get_roll_and_seeds(nonce, server_seed, client_seed)
                    connection.sendall(f"Client seed: {client_seed}\nNonce: {nonce}\n".encode())
                    # print(f'\nRoll for nonce {nonce} is {roll}')data = connection.recv(BYTE_RECV).decode().strip()
                    status = False
                    f.write("Client Seed "+client_seed + "|\n")
                    f.write("Server Seed " +server_seed + "|\n")
                    #f.write("Nounce " +nonce + "|\n")
                    data = connection.recv(BYTE_RECV).decode().strip()
                    if data =="heads" or data =="tails":
                        client_answer = data
                        
                    if roll <= 50:
                        server_answer = "heads"
                        connection.sendall("The result of the coin flip is heads!\n".encode())
                        print("The result of the coin flip is heads!\n")
                    else:
                        server_answer = "tails"
                        connection.sendall("The result of the coin flip is tails!\n".encode())
                        print("The result of the coin flip is tails!\n")
                    print(f"Server answer:{server_answer}")
                    print(f"Client answer:{client_answer}")
                    f.write("Client Answer "+client_answer +"|\n")
                    f.write("Server Answer "+server_answer +"|\n")
                    if client_answer != server_answer:
                        connection.sendall("player have lost".encode())
                        # print("player have lost")
                    else:
                        connection.sendall("player have won".encode())
                    
                        # print("The result of the coin flip is tails!\n")
        #          Append variables to text file
        #          Need to store client seed, server seed, nonce, roll, result.
                elif data == "2":
                    pass
                elif data == "3":
                    changeSeed = "User want to change"
                    data = connection.recv(BYTE_RECV).decode().strip()
                    print(data)
                    client_seed = data
                    # client_seed = main.generate_client_seed(client_seed, changeSeed)[0]
                    changeSeed = "User has changed"
        return

try:
    while True:
        # try:
            connection, client_address = sock.accept()
            thread = threading.Thread(target=handle_client, args=(connection, client_address), daemon = True)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        # except socket.timeout:
            # print("Timeout")
            # pass

except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing server socket.")
    sock.close()
    sys.exit(0)

print("[STARTING] server is starting...")

