import socket
import ssl 

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_verify_locations('key/new.pem')

server_address = ('localhost', 10000)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_soc=context.wrap_socket(sock,server_hostname='localhost')
# Connect the socket to the port where the server is listening
print(f'connecting to {server_address[0]} port {server_address[1]}')
c_soc.connect(server_address)

try:
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
    print('closing socket')
    sock.close()
