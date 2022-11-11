import random
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
print('Connected to the server.')

n = int(client.recv(1024).decode('ascii'))
g = int(client.recv(1024).decode('ascii'))

b = random.randint(5, 55)
B = (g**b)%n

A = int(client.recv(1024).decode('ascii'))
client.send(str(B).encode('ascii'))

secret_key = (A**b)%n
print(f'Secret Key is {secret_key}')