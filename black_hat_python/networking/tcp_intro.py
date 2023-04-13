import socket

target_host = '0.0.0.0'
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b'GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n')

# receive some data
tcp_response = client.recv(4096)

print(tcp_response.decode())
with open('tcp_response.html', 'w') as f:
    f.write(tcp_response.decode())
client.close()
