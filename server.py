import socket
import threading
import sys
import json
import main
import ssl
import os

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('key/certificate.crt','key/private.key')

#params
SERVER = socket.gethostbyname(socket.gethostname())
SERVER_NETWORK='0.0.0.0' #Use this when connecting over the network 
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
sock.settimeout(5)
sock.listen(2)
print('waiting for a connection')

s_sock = context.wrap_socket(sock, server_side=True)

def handle_client(connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    connected = True
    status = True
    nonce = 0
    changeSeed = "No need change"
    client_seed = "GoingToBeChanged"
    server_seed = "GoingToBeChanged"
    file_name = f"{client_address[0]}_{client_address[1]}.json" #set to .json/.txt for simple viewing

    while connected:
        try:
            data = connection.recv(BYTE_RECV).decode().strip()
            if data == DISCONNECT_MESSAGE:
                if os.path.isfile(file_name):
                    with open(file_name, 'rb') as file:
                        data = file.read()
                        connection.sendall(len(data).to_bytes(4, byteorder='big'))
                        connection.sendall(data)
                    print('File has been transferred successfully.')
                else:
                    print("Error, no result".encode())
                connected = False
                connection.close()
                print(f"[DISCONNECTED] {client_address} disconnected.")
                #FH.convert_text_to_json(file_name, "Result.json") #should be able to remove this conversion
            elif len(data) != 0:
                if data == "1":
                    client_answer = ""
                    server_answer = ""

                    nonce = main.get_nonce(nonce, status)[0]
                    server_seed = main.generate_server_seed(server_seed)
                    client_seed, changeSeed = main.generate_client_seed(client_seed, changeSeed)
                    roll, server_seed, client_seed = main.get_roll_and_seeds(nonce, server_seed, client_seed)
                    connection.sendall(f"Client seed: {client_seed}\nNonce: {nonce}\n".encode())
                    status = False
                    
                    data = connection.recv(BYTE_RECV).decode().strip()
                    if data =="heads" or data =="tails":
                        client_answer = data
                    connection.sendall((f"Roll result: {roll}").encode())    
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

                    #Open file
                    if os.path.isfile(file_name):
                        with open(file_name, 'r') as file:
                            data = json.load(file)
                    else:
                        data = []
                        # with open(file_name, "a") as f:
                    new_data = {'Client Seed' :client_seed,
                        'Server Seed' : server_seed, 
                        'Client Answer': client_answer, 
                        'Server Answer':server_answer, 
                        'Nounce' : str(nonce)}
                    data.append(new_data)
                    with open(file_name, 'w') as f:
                        json.dump(data, f,indent=4)


                    if client_answer != server_answer:
                        connection.sendall("player have LOST!".encode())
                    else:
                        connection.sendall("player have WON!".encode())
                    
                elif data == "2":
                    changeSeed = "User want to change"
                    data = connection.recv(BYTE_RECV).decode().strip()
                    print(data)
                    client_seed = data
                    changeSeed = "User has changed"
        except Exception as exc:
            print(exc)
            break
    return

try:
    while True:
        try:
            connection, client_address = s_sock.accept()
            thread = threading.Thread(target=handle_client, args=(connection, client_address), daemon = True)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except socket.timeout:
            pass

except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing server socket.")
    sock.close()
    sys.exit(0)

