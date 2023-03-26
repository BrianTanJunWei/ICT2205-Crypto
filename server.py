import socket
import threading
import sys
import json
import main
import time
import time
import os

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
<<<<<<< HEAD
sock.settimeout(5)
=======
# sock.settimeout(5)
>>>>>>> YuXiang
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
    file_name = f"{client_address[0]}_{client_address[1]}.json" #set to .json/.txt for simple viewing

    while connected:
<<<<<<< HEAD
        try:
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
                        'Server Seed' : server_seed, 
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
                    # pass
                elif data == "2":
                    changeSeed = "User want to change"
                    data = connection.recv(BYTE_RECV).decode().strip()
                    print(data)
                    client_seed = data
                    # client_seed = main.generate_client_seed(client_seed, changeSeed)[0]
                    changeSeed = "User has changed"
        except Exception as exc:
            print(exc)
            break
=======
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
                    'Server Seed' : server_seed, 
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
>>>>>>> YuXiang
    return

try:
    while True:
<<<<<<< HEAD
        try:
=======
        # try:
>>>>>>> YuXiang
            connection, client_address = sock.accept()
            thread = threading.Thread(target=handle_client, args=(connection, client_address), daemon = True)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
<<<<<<< HEAD
        except socket.timeout:
            # print("Timeout")
            pass
=======
        # except socket.timeout:
            # print("Timeout")
            # pass
>>>>>>> YuXiang

except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing server socket.")
    sock.close()
    sys.exit(0)

print("[STARTING] server is starting...")

