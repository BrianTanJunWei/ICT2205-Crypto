import socket
<<<<<<< Updated upstream
import ssl 
=======
import sys
import json
>>>>>>> Stashed changes

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('key/new.pem')

server_address = ('localhost', 10000)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_soc=context.wrap_socket(sock,server_hostname='localhost')
# Connect the socket to the port where the server is listening
print(f'connecting to {server_address[0]} port {server_address[1]}')
c_soc.connect(server_address)

try:
<<<<<<< Updated upstream
    # Send data
    message = b'This is the message. It will be repeated.'
    print(f'sending {message!r}')
    c_soc.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = c_soc.recv(1024)
        amount_received += len(data)
        print(f'received {data!r}')
finally:
=======
    # send("Authenticated")

    connect = True
    while connect:
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
            print(json_data)
            with open('client-file.json', 'w') as file:
                 json.dump(json_data ,file,indent=4)

            print('File has been received successfully.')

        else:
             print("Invalid input please try again\n")

        
    
>>>>>>> Stashed changes
    print('closing socket')
    sock.close()
