import socket

def port_scanner(target_ip, port):
  if(target_ip is None or  port is None):
       print('Please provide a port')
       return
  s = socket.socket()
  s.settimeout(3)
  try:
    s.connect((target_ip, port))
    #print('Port ',port,': closed') 
    print(f"port {port}: open")
  except ConnectionRefusedError:
    print('Port ',port,': closed')
  except socket.timeout : 
    print(f"port {port}: timed out")  
  finally:
    s.close() # we should close socket when it finish running
    
target_ip = input('Enter Target IP : ')
try : 
  #input weill always give string we have to convert that to integer to use in range cause range has to be integer
  
  start_port = int(input('Enter starting port : '))
  ending_port = int(input('Enter ending port : '))
  
  ports = range(start_port, ending_port + 1) # to scan from port 1 to 100

  for port in ports:
    port_scanner(target_ip, port)
  
except ValueError:  # to avoid string error when number is wanted (enter port number : abc we dont want that right?)
  print('Please enter a valid number')
  



    

  
