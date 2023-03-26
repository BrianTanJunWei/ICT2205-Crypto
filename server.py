import socket
<<<<<<< Updated upstream
import ssl 

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('key/new.pem','key/private.key')


# context.options |= ssl.OP_NO_TLSv1_3 ## op out of tls 1.3
# context.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256:')
=======
import threading
import sys
import json
import main
import time
import FileHandler as FH
import main
import time
import os
>>>>>>> Stashed changes


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(2) #listen to 2 connection, client A and client B

s_sock = context.wrap_socket(sock, server_side=True)

<<<<<<< Updated upstream
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = s_sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print(f'received {data!r}')
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from ', client_address)
            break
    finally:
    # Clean up the connection
        connection.close()
=======

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
        data = connection.recv(BYTE_RECV).decode().strip()
        if data == DISCONNECT_MESSAGE:
            if os.path.isfile(file_name):
                # connection.sendall("ok".encode())
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
                # print(f'\nRoll for nonce {nonce} is {roll}')data = connection.recv(BYTE_RECV).decode().strip()
                status = False
                # f.write("Client Seed "+client_seed + "|\n")
                # f.write("Server Seed " +server_seed + "|\n")
                
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

                #Open file
                if os.path.isfile(file_name):
                # connection.sendall("ok".encode())
                    with open(file_name, 'r') as file:
                         data = json.load(file)
                else:
                    data = []
                    # with open(file_name, "a") as f:
                new_data = {'Client Seed' :client_seed,
                    'Server Seed ' : server_seed, 
                    'Client Answer': client_answer, 
                    'Server Answer':server_answer, 
                    'Nounce' : str(nonce)}
                data.append(new_data)
                with open(file_name, 'w') as f:
                    json.dump(data, f,indent=4)
                    #     json.dump(x,f,indent=4)
                    #     f.write('\n')
                    #     f.close()


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
                # pass
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

>>>>>>> Stashed changes
