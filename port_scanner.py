import socket
import sys
import ipaddress

def port_scanner(target_ip, port):
     
  s = socket.socket()
  s.settimeout(3)
  
  try:
    s.connect((target_ip, port))
    # print('Port ',port,': closed') 
    # print(f"port {port}: open") 
              #or
    return "open"
    
  except ConnectionRefusedError:
    # print('Port ',port,': closed')
    return 'closed'
    
  except socket.timeout : 
    #print(f"port {port}: timed out")  
    return 'timed out'
  
  finally:
    s.close() # we should close socket when it finish running
    

try : 
  #input weill always give string we have to convert that to integer to use in range cause range has to be integer
  
  target_ip = input('Enter Target IP : ') 
  target = ipaddress.ip_address(target_ip) # this can tell us whether an ip is private
  
  if target.is_private:
    print('Private IP')
  else:
    print('Only private IP addresses are allowed')
    sys.exit()
    
  start_port = int(input('Enter starting port : '))
  ending_port = int(input('Enter ending port : '))
  
  if start_port < 1 or ending_port > 65535 or start_port > ending_port :
    print('Invalid Port Range')
    sys.exit() # used this instead of return cause return can't be used directly at the top leval of our script meaning it has to in function 
    
    # sys.exit() means stop executing this programm now
  
  ports = range(start_port, ending_port + 1) # to scan from port 1 to 100

  for port in ports:
    # target is ipv4address object , not a normal string, so we need to convert that into string
   result = port_scanner(str(target), port)
   
   if result == 'open':
     print(f"Port {port} is open")
   elif result == 'closed':
     print(f"port {port} is closed")
   elif result == 'timed out':
     print(f'port {port} is timed out')
     
except ValueError:  # to avoid string error when number is wanted (enter port number : abc we dont want that right?)
  print('Please enter a valid number')
  



    

  
