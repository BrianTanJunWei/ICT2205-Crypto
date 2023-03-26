import socket
import sys
import os
import main
import json

def send(msg):
        # Send data
        message = msg
        # print('sending {!r}'.format(message))
        sock.sendall(message.encode())

#params
<<<<<<< HEAD
SERVER = "192.168.1.9" #change according to the localhost ip address
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
start_game = False
=======
SERVER = "192.168.56.1" #change according to the localhost ip address
PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
>>>>>>> YuXiang

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
<<<<<<< HEAD
        try:
            print("Welcome To Coin Flip!")
            print("Enter '1' To Start New Game")
            print("Enter '2' To Change Client Seed")
            print("Enter '3' To End The Program")
            #print("This is changeSeed: " + changeSeed)
            message = input("\nPlease choose an option: ")
            if message == "1":
                start_game = True
                send(message)
                from_server = sock.recv(4096).decode()
                print(from_server.strip())
                message = input("Input your guess (heads/tails): ")
                # check if player correct input the correct answer
                answer = True
                while answer:
                    if message == "heads" or message == "tails":
                        answer = False
                    else:
                        print("error input please try again!")
                        message = input("Input your guess (heads/tails): ")
                send(message)
                from_server = sock.recv(4096).decode()
                print("\n"+from_server.strip())
                from_server = sock.recv(4096).decode()
                print(from_server.strip())
                print("\nTo continue input 1 again.\n")
            elif message == "2":
                send(message)
                message = input("Enter your client seed: ")
                send(message)
            elif message == "3":
                connect = False
                send(DISCONNECT_MESSAGE)
                if start_game == True:
                    # Write File in binary
                    data_len = int.from_bytes(sock.recv(4), byteorder='big')
                    data = sock.recv(data_len)
                    json_data = json.loads(data)
                    with open('client-file.json', 'w') as file:
                        json.dump(json_data ,file,indent=4)

                    print('File has been received successfully.')

            else:
                print("Invalid input please try again\n")
        except Exception as exc:
            print(exc)
            break
=======
        print("Welcome To Coin Flip!")
        print("Enter '1' To Start New Game")
        print("Enter '2' To Verify Roll")
        print("Enter '3' To Change Client Seed")
        print("Enter '4' To End The Program")
        #print("This is changeSeed: " + changeSeed)
        message = input("\nPlease choose an option: ")
        if message == "1":
            send(message)
            from_server = sock.recv(4096).decode()
            print(from_server.strip())
            message = input("Input your guess (heads/tails): ")
            # check if player correct input the correct answer
            answer = True
            while answer:
                if message == "heads" or message == "tails":
                    answer = False
                else:
                     print("error input please try again!")
                     message = input("Input your guess (head/tails): ")
            send(message)
            from_server = sock.recv(4096).decode()
            print("\n"+from_server.strip())
            from_server = sock.recv(4096).decode()
            print(from_server.strip())
            print("\nTo continue input 1 again.\n")
        elif message == "2":
            pass
        elif message == "3":
             send(message)
             message = input("Enter your client seed: ")
             send(message)
        elif message == "4":
            connect = False
            send(DISCONNECT_MESSAGE)
            # Write File in binary
            data_len = int.from_bytes(sock.recv(4), byteorder='big')
            data = sock.recv(data_len)
            json_data = json.loads(data)
            with open('client-file.json', 'w') as file:
                 json.dump(json_data ,file,indent=4)

            print('File has been received successfully.')

        else:
             print("Invalid input please try again\n")
>>>>>>> YuXiang

        
    
    print('closing socket')
    sock.close()
    
except KeyboardInterrupt:
    print("Ctrl+C pressed. Closing client socket.")
    send(DISCONNECT_MESSAGE)
    sock.close()
    sys.exit(0)

    
    
