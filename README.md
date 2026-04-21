# Threat Recon 🔎

Outil Python d'investigation CTI — analyse complète d'un domaine ou d'une IP en quelques secondes.

## Fonctionnalités

- **WHOIS** — registrar, dates de création/expiration, organisation, pays
- **DNS** — enregistrements A, MX, NS, TXT
- **Géolocalisation IP** — pays, ville, FAI, organisation
- **VirusTotal** — vérification de la réputation du domaine contre 90+ moteurs antivirus

## Utilisation

```bash
pip install requests python-whois dnspython python-dotenv
python threat_recon.py
Créez un fichier .env avec votre clé API VirusTotal :

VT_API_KEY=votre_clé_ici
Entrez un domaine (ex: google.com) et l'outil récupère toutes les informations en quelques secondes.

Exemple de résultat
[*] WHOIS — google.com
Registrar     : MarkMonitor, Inc.
Creation      : 15/09/1997
Expiration    : 14/09/2028
Organisation  : Google LLC
[*] VirusTotal — google.com
Verdict       : CLEAN
Malveillant   : 0/90 moteurs
Contexte
Outil développé pour automatiser la phase de reconnaissance lors d'investigations CTI — cartographie des actifs numériques, analyse DNS, vérification de réputation.

Complémentaire au projet CVE Watch.
