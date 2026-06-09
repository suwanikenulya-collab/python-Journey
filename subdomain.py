#START

#INPUT domain

#subdomains = [www, mail, admin, api, blog, dev, test, ftp, shop, portal]

#PRINT "Searching for subdomains..."

#FOR each subdomain in subdomains

   # full_domain = subdomain + "." + domain

   # TRY

       # ip_address = DNS lookup(full_domain)

        #PRINT full_domain and ip_address

 #   EXCEPT

#        Do nothing

#END FOR

#PRINT "Scan complete!"

#END
# we use socket cuz it can perform a DNS lookup

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

print("\nScan complete!")