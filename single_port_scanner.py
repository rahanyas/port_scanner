# need a way to communicate with a mchine over the network python has built-in socket module

import socket

s = socket.socket() # creates a netwrok socket object

# print(s)

# socket doesn't know where to connect so we need two things 
 # ip address -> which machine
 # port -> which service
 
target = '127.0.0.1' # my machine
port = 80

# now we need to tell s try connect to this target and this port

s.connect((target, port))

# if we run this it will crash , cause if somthing listening , the programm will continue without the error will get <ConnectionRefusedError>