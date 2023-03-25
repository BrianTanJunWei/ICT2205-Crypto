import socket
import threading
import sys
<<<<<<< Updated upstream
import json
=======
import main
import time
import FileHandler as FH
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    file_name = f"{client_address[0]}_{client_address[1]}.txt"
    with open(file_name, "w") as f:
        f.write("Hello, world!")
=======
    nonce = 0
    changeSeed = "No need change"
    client_seed = "GoingToBeChanged"
    server_seed = "GoingToBeChanged"
    status = True
    #Open file
    file_name = f"{client_address[0]}_{client_address[1]}.txt"
    with open(file_name, "a") as f:
        
        while connected:
            data = connection.recv(BYTE_RECV)
            print(data)
        
            if data.decode().strip() == DISCONNECT_MESSAGE:
                connected = False
                connection.close()
                print(f"[DISCONNECTED] {client_address} disconnected.")
                FH.convert_text_to_json(file_name, "Result.json")
            elif len(data) != 0:
                print("testing")
                if data.decode().strip() == "1":
                    print("entered 1")
                    nonce = main.get_nonce(nonce, status)[0]
                    server_seed = main.generate_server_seed(server_seed)
                    client_seed, changeSeed = main.generate_client_seed(client_seed, changeSeed)
                    roll, server_seed, client_seed = main.get_roll_and_seeds(nonce, server_seed, client_seed)
                    print(f'\nRoll for nonce {nonce} is {roll}')
                    f.write("Client Seed "+client_seed + "|\n")
                    #f.write("Server Seed " +server_seed + "|\n")
                    status = False
                    if roll <= 50:
                        print("The result of the coin flip is heads!\n")
                    if roll > 50:
                        print("The result of the coin flip is tails!\n")
        #          Append variables to text file
        #          Need to store client seed, server seed, nonce, roll, result.
                if data.decode().strip() == "2":
                    f.write("Client Seed "+client_seed + "|\n")
                    #f.write("Server Seed " +server_seed + "|\n")
                    # variables Decision/Client_seed/Server_seed/nounce/Result
                    # should be appending continously
                    
        return 
>>>>>>> Stashed changes

        while connected:
            data = connection.recv(BYTE_RECV)
            if data.decode().strip() == DISCONNECT_MESSAGE:
                connected = False
                connection.close()
                f.close()
                print(f"[DISCONNECTED] {client_address} disconnected. File written: {file_name}")
                convert_text_to_json(file_name, "json_log.json") 
            elif len(data) != 0:
                f.write(data.decode())

def convert_text_to_json(input_file, output_file):
    # Open the input file and read the lines
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Create a list to hold the dictionaries
    data = []

    # Iterate over the lines and parse them into dictionaries
    for line in lines:
        # Parse the line into fields
        fields = line.strip().split("|")

        # Create a dictionary with the fields as keys and values
        d = {
            "Client Seed": fields[0],
            # Add more fields as needed
        }

        # Append the dictionary to the list
        data.append(d)

    # Write the list of dictionaries to the output file as JSON
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
                

def start():
    sock.listen(2) #listen to 2 connection, client A and client B
    print('waiting for a connection')
    while True:
        connection, client_address = sock.accept()
        thread = threading.Thread(target=handle_client, args=(connection, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
try:
    print("[STARTING] server is starting...")
    start()
except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing server socket.")
    sock.close()
    sys.exit(0)

<<<<<<< Updated upstream
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
=======
print("[STARTING] server is starting...")

>>>>>>> Stashed changes
