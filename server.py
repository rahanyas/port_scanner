import socket

s = socket.socket()

host = '127.0.0.1'

port = 9999

s.bind((host, port))

s.listen()

print('server startd...')

connection, address = s.accept()

print(address)