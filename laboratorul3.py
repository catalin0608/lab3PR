import socket

dns_server = None  # Variabila pentru a stoca DNS-ul folosit

def resolve_domain(domain):
    try:
        resolved_ips = socket.gethostbyname_ex(domain)
        print(f"Adrese IP pentru domeniul '{domain}': {', '.join(resolved_ips[2])}")
    except socket.gaierror as e:
        print(f"Nu s-au putut găsi adrese IP pentru domeniul '{domain}': {str(e)}")

def resolve_ip(ip):
    try:
        resolved_domains = socket.gethostbyaddr(ip)
        print(f"Domenii asociate adresei IP '{ip}': {', '.join(resolved_domains[0])}")
    except socket.herror as e:
        print(f"Nu s-au putut găsi domenii pentru adresa IP '{ip}': {str(e)}")

while True:
    command = input("Introduceți comanda: ")

    # Verificăm comanda "resolve" - startswith pentru verificare șiruri de caractere
    if command.startswith("resolve"):
        parts = command.split(" ")
        if len(parts) == 2:
            target = parts[1]

            # Verificăm dacă este domeniu sau adresă IP
            if target.count(".") >= 3:  # Dacă conține cel puțin 3 puncte, este adresă IP
                resolve_ip(target)
            else:
                resolve_domain(target)

    # Verificăm comanda "use dns"
    elif command.startswith("use dns"):
        parts = command.split(" ")
        if len(parts) == 3:
            dns_ip = parts[2]
            try:
                # Verificăm dacă adresa IP a DNS-ului este validă
                socket.inet_aton(dns_ip)
                dns_server = dns_ip
                print(f"DNS-ul a fost schimbat și va fi utilizat adresa IP: {dns_ip}")
            except socket.error:
                print("Adresa IP a DNS-ului este invalidă")

    # Verificăm comanda "exit"
    elif command == "exit":
        break

    # Comanda nu este recunoscută
    else:
        print("Comandă necunoscută")

