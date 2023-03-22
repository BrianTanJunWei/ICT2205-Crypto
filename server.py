import socket
import ssl 

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('key/new.pem','key/private.key')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(2) #listen to 2 connection, client A and client B

s_sock = context.wrap_socket(sock, server_side=True)

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
