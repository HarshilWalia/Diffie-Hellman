import random
import socket
import time
from sympy import *

host = "127.0.0.1" 
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, address = server.accept()
print(f'{address} connected.')

primes = [i for i in range(201, 500) if isprime(i)]
n = random.choice(primes)
client.send(str(n).encode('ascii'))
time.sleep(0.5) # Server sends the keys at a faster rate compared to the acceptance rate of the client, So we have to make sure that the server waits for the client to recieve the keys

primes = [i for i in range(00, 200) if isprime(i)]
g = random.choice(primes)

client.send(str(g).encode('ascii'))

a = random.randint(56, 95)

A = (g**a)%n
time.sleep(1) # same reason

client.send(str(A).encode('ascii'))
B = int(client.recv(1024).decode('ascii'))


secret_key = (B**a)%n

print(f'Secret Key is {secret_key}')