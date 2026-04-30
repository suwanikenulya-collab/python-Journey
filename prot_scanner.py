import socket
from datetime import datetime #use to get current date and time.

target = input("Enter the target IP address: ")

def port_scan(target): #takes target as the input and encapsulates scanning logic
    #error handling
    try:
        ip = socket.gethostbyname(target) #coverts domain-> IP address
        print(f"Scanning the target {ip}")
        print("Time started:", datetime.now())

        for port in range(30, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket object. AF_INET->IPV4 and SOCK_STREAM-> TCP connection
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")

            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved")

    except socket.error:
        print("Couldn't connect to server")

port_scan(target)