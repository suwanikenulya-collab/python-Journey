import socket

# Get domain from user
domain = input("Enter a domain (e.g. google.com): ")

# Common subdomains to check
subdomains = [
    "www",
    "mail",
    "admin",
    "api",
    "blog",
    "dev",
    "test",
    "ftp",
    "shop",
    "portal"
]

print("\nSearching for subdomains...\n")

for subdomain in subdomains:
    full_domain = f"{subdomain}.{domain}"

    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[FOUND] {full_domain} -> {ip}")

    except socket.gaierror:
        pass

print("\nScan complete!"