import socket
import sys
import json
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('key/certificate.crt')

def send(msg):
        # Send data
        message = msg
        c_soc.sendall(message.encode())

#params
SERVER = "172.18.192.1" #change according to the localhost ip address
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
start_game = False

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_soc=context.wrap_socket(sock,server_hostname='localhost')
# Connect the socket to the port where the server is listening
server_address = (SERVER,PORT)
print('connecting to {} port {}'.format(*server_address))
c_soc.connect(server_address)

try:
    # send("Authenticated")

    connect = True
    while connect:
        try:
            print("Welcome To Coin Flip!")
            print("Enter '1' To Start New Game")
            print("Enter '2' To Change Client Seed")
            print("Enter '3' To End The Program")
            message = input("\nPlease choose an option: ")
            if message == "1":
                start_game = True
                send(message)
                from_server = c_soc.recv(4096).decode()
                print(from_server.strip())
                message = input("\nInput your guess (heads/tails): ")
                # check if player correct input the correct answer
                answer = True
                while answer:
                    if message == "heads" or message == "tails":
                        answer = False
                    else:
                        print("error input please try again!")
                        message = input("Input your guess (heads/tails): ")
                send(message)
                from_server = c_soc.recv(4096).decode()
                print("\n"+from_server.strip())               
                from_server = c_soc.recv(4096).decode()
                print("\n"+from_server.strip())
                from_server = c_soc.recv(4096).decode()
                print(from_server.strip())
                print("\nTo continue input 1 again.\n")
            elif message == "2":
                send(message)
                message = input("\nEnter your client seed: ")
                send(message)
            elif message == "3":
                connect = False
                send(DISCONNECT_MESSAGE)
                if start_game == True:
                    # Write File in binary
                    data_len = int.from_bytes(c_soc.recv(4), byteorder='big')
                    data = c_soc.recv(data_len)
                    json_data = json.loads(data)
                    with open('client-file.json', 'w') as file:
                        json.dump(json_data ,file,indent=4)

                    print('File has been received successfully.')

            else:
                print("Invalid input please try again\n")
        except Exception as exc:
            print(exc)
            break

        
    
    print('closing socket')
    c_soc.close()
    
except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing client socket.")
    send(DISCONNECT_MESSAGE)
    c_soc.close()
    sys.exit(0)

    
    
