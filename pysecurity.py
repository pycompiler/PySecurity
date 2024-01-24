try:
    import requests
    import os
    import json
    from colorama import Fore
except Exception:
    print("Your Modules Are Missing.")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

def print_menu():
    MENU = f"""{Fore.LIGHTGREEN_EX}
    MRX - PySecurity | https://github.com/MrX0955
    If it gives an error saying {Fore.RED}'Quota Limit'{Fore.LIGHTGREEN_EX}, change your IP.

    [0] > Close ForensicTool.        
    [1] > Reverse DNS.              
    [2] > DNS Lookup.                
    [3] > Geolocation IP.           
    [4] > Zone Transfer.             
    [5] > DNS Host Records.         
    [6] > Reverse IP Lookup.
    [7] > ASN Lookup.           
    """
    print(MENU)

def reverseDNS():
    print(f"{Fore.LIGHTRED_EX} > Reverse DNS | (8.8.8.8){Fore.LIGHTGREEN_EX}")
    dns = input("Enter the IP Address: ")
    izlegal = requests.get(f"https://api.hackertarget.com/reversedns/?q={dns}")
    print(izlegal.text, "| >> Press ENTER For Exit.")
    input()

def DNSLookup():
    print(f"{Fore.LIGHTRED_EX} > DNS Lookup | (example.com){Fore.LIGHTGREEN_EX}")
    lookup = input("Enter the Domain Name: ")
    two = requests.get(f"https://api.hackertarget.com/dnslookup/?q={lookup}")
    print(two.text, "| >> Press ENTER For Exit.")
    input()

def geoip():
    print(f"{Fore.LIGHTRED_EX} > Geolocation IP | (8.8.8.8){Fore.LIGHTGREEN_EX}")
    geoip = input("Enter the IP Address: ")
    i = requests.get(f"https://api.hackertarget.com/ipgeo/?q={geoip}")
    print(i.text), "| => Press ENTER For Exit."
    input()

def zonetransfer():
    print(f"{Fore.LIGHTRED_EX} > Zone Transfer | (8.8.8.8){Fore.LIGHTGREEN_EX}")
    zonetransfer = input("Enter the IP Address: ")
    z = requests.get(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")
    print(z.text), "| => Press ENTER For Exit."
    input()

def dnssubdomain():
    print(f"{Fore.LIGHTRED_EX} > DNS Subdomain check | (example.com){Fore.LIGHTGREEN_EX}")
    subdomain = input("Enter the Domain Name: ")
    k = requests.get(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")
    print(k.text), "| => Press ENTER For Exit."
    input()

def reverseip():
    print(f"{Fore.LIGHTRED_EX} > Reverse IP Lookup | (8.8.8.8){Fore.LIGHTGREEN_EX}")
    reverseip = input("Enter the IP Address: ")
    mrx = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")
    print(mrx.text), "| => Press ENTER For Exit."
    input()

def ASN():
    print(f"{Fore.LIGHTRED_EX} > ASN Lookup | (8.8.8.8){Fore.LIGHTGREEN_EX}")
    asnlookup = input(" IP Address or ASN: ")
    hasfa = requests.get(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")
    print(hasfa.text), "| => Press ENTER For Exit."
    input()


while True:
    print_menu()
    choice = int(input("Choose an option: "))

    if choice == 0:
        exit()

    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


    if choice == 1:
        reverseDNS()

    elif choice == 2:
        DNSLookup()

    elif choice == 3:
        geoip()

    elif choice == 4:
        zonetransfer()

    elif choice == 5:
        dnssubdomain()

    elif choice == 6:
        reverseip()

    elif choice == 7:
        ASN()
