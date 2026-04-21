import whois
import dns.resolver
import requests
import socket

def print_banner():
    print("=" * 60)
    print("        OSINT TOOL — Domain & IP Investigation")
    print("=" * 60)

def get_whois(domain):
    print(f"\n[*] WHOIS — {domain}")
    print("-" * 40)
    try:
        w = whois.whois(domain)
        creation = w.creation_date
        expiration = w.expiration_date
        if isinstance(creation, list):
            creation = creation[0]
        if isinstance(expiration, list):
            expiration = expiration[0]
        print(f"Registrar     : {w.registrar}")
        print(f"Creation      : {creation.strftime('%d/%m/%Y') if creation else 'N/A'}")
        print(f"Expiration    : {expiration.strftime('%d/%m/%Y') if expiration else 'N/A'}")
        print(f"Organisation  : {w.org}")
        print(f"Pays          : {w.country}")
    except Exception as e:
        print(f"[!] Erreur WHOIS : {e}")

def get_dns(domain):
    print(f"\n[*] DNS Records — {domain}")
    print("-" * 40)
    for record in ["A", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, record)
            for r in answers:
                print(f"{record.ljust(5)} : {r}")
        except:
            print(f"{record.ljust(5)} : Aucun enregistrement")

def get_ip_info(domain):
    print(f"\n[*] IP & Geolocalisation — {domain}")
    print("-" * 40)
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP            : {ip}")
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        print(f"Pays          : {data.get('country')}")
        print(f"Ville         : {data.get('city')}")
        print(f"FAI           : {data.get('isp')}")
        print(f"Organisation  : {data.get('org')}")
    except Exception as e:
        print(f"[!] Erreur IP : {e}")

# === MAIN ===
print_banner()
domain = input("\nEntrez un domaine a analyser : ").strip()
get_whois(domain)
get_dns(domain)
get_ip_info(domain)
print("\n" + "=" * 60)
print("Analyse terminee.")
print("=" * 60)