import subprocess
import socket
import sys

def ping_host(ip):
    """ Vérifie si l'hôte est actif via un ping"""
    try:
        output = subprocess.run(
            ["ping","-c","1","-W","2",ip],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL
        )
        if output.returncode == 0:
            print(f"\n[+] L'hôte {ip} est ACTIF (UP)")
            return True
        else:
            print(f"\n[-] L'hôte {ip} est INACTIF (DOWN)")
            return False
    except Exception as e:
        print(f"Erreur lors du ping : {e}")
        return False

def scan_ports(ip,ports):
    """Scanne une liste de ports TCP sur l'hôte cible"""
    print(f"[*] Début du scan des ports sur {ip}...")
    for port in ports:
        # Création d'un socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Timeout de 1 seconde pour éviter de bloquer 

        try:
            # Tentative de connextion sur le port 
            result = s.connect_ex((ip,port))
            if result  == 0:
                print(f"[OPEN] Le port {port} est OUVERT")
            else:
                pass # Le port est fermé, on n'affiche rien pour garder un affichage propre
        except socket.error:
            print(f"[ERROR] Impossible de se connecter au port {port}")
        finally:
            s.close()



if __name__ == "__main__":
    target = input("Enter l'addresse IP à tester : ")
    
    if ping_host(target):
        #Liste de quelques ports courants à tester  (SSH, HTTP, HTTPS, FTP, etc...)
        ports_to_scan = [21,22,80,443,8080]
        scan_ports(target, ports_to_scan)