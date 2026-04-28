import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        sock.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def main():
    target = input("Enter target (IP or domain): ")

    print(f"\nScanning target: {target}\n")

    for port in range(20, 1025):  # common ports
        scan_port(target, port)


if __name__ == "__main__":
    main()