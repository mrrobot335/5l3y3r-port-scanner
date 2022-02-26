import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER BY 5l3y3r")
print(ascii_banner)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input ('[+] Enter Target IP: ')
def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False

for portNumber in range(1,100):
    print("Scanning port", portNumber)
    if scanner(portNumber):
        print('[+] Port', portNumber, '/tcp', 'is open!')
